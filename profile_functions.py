import os, csv, random
import hsk_repository as hr
from chinese import ChineseAnalyzer
import dictionary_repository as dr
from datetime import datetime
import auxilliary_functions as aux

analyzer = ChineseAnalyzer()

print('''Welcome to A Journey Eastward
A Chinese language code project by Fritz Stevenson
You will input a list of characters or phrases, 
select the size of the quiz, then answer a variety
of randomized questions regarding the entered vocabulary.''')

'''Bug Log
ProfileObject.list_append is not recognized

When the csv files are imported from the profiles folder, everything is in string format. Some need to be in float, 
some need to be in int
'''

'''Change Plans
--Need two different entry systems: one as a solid text block and one as the hsk_vocab list format. Also need a function 
to clean unnecessary special characters and letters from input.
'''




class ProfileObject:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        if not self.check_if_profile_exists():
            self.make_profile_folder()
            self.check_to_add_characters()
            self.create_profile()
            self.save_files()
        else:
            self.fetch_csv_to_dict()
        self.list = self.instantiate_character_list()
        self.list_appends = []

        self.analyzer = ChineseAnalyzer()
        self.quit_token = False
        self.HSK_Level = int(dr.profile_dictionary['HSK_Level'])
        self.HSk_points = [dr.HSK_dictionary['HSK1 Points'],
                           dr.HSK_dictionary['HSK2 Points'],
                           dr.HSK_dictionary['HSK3 Points'],
                           dr.HSK_dictionary['HSK4 Points'],
                           dr.HSK_dictionary['HSK5 Points'],
                           dr.HSK_dictionary['HSK6 Points']
                           ]
        self.HSK_thresholds = [dr.HSK_dictionary['HSK1 Threshold'],
                               dr.HSK_dictionary['HSK2 Threshold'],
                               dr.HSK_dictionary['HSK3 Threshold'],
                               dr.HSK_dictionary['HSK4 Threshold'],
                               dr.HSK_dictionary['HSK5 Threshold'],
                               dr.HSK_dictionary['HSK6 Threshold']
                                ]
        print(dr.character_dictionary)
        while not self.quit_token:
            self.serve_question()

    def serve_question(self):
        """Administers a randomized question and calls check_for_quit and assign_calculated adjustments."""
        char = self.list[random.randint(0, len(self.list))-1]
        print(char)
        zh_object = self.analyzer.parse(char)
        token = zh_object.tokens()[0]
        definition = zh_object[token][0].definitions
        pinyin = zh_object[token][0].pinyin
        approach = aux.approach_roll()
        answer_bool = None
        if approach == 0:
            answer = input(f'What is the meaning of {token}')
            if answer in definition:
                print('True')
                answer_bool = True
            else:
                print('False')
                answer_bool = False
        if approach == 1:
            answer = input(f'How would you pronounce {token} in pinyin?:  ')
            if answer == ''.join(pinyin).lower():
                print('True')
                answer_bool = True
            else:
                print('False')
                answer_bool = False
        if approach == 2:
            answer = input(f'What character(s) mean ({definition})?:  ')
            if answer == token:
                print('True')
                answer_bool = True
            else:
                print('False')
                answer_bool = False
        if approach == 3:
            print(f'Entering a special round! Your character is {token}\n')
            answer = input('Enter a definition, the correct pinyin and tone, or ')
            answer_bool = True
        if aux.check_for_quit(answer):
            self.quit_token = True

        self.adjust_hsk_points(token, aux.calculated_adjustments(token, answer_bool))

        self.check_to_add_characters()
        print(token, pinyin, definition)

    def serve_question_easy(self):
        pass

    def check_for_hsk_levelup(self):
        pass

    def check_to_add_characters(self):
        """Checks if there are Enough HSK_Points to add new characters to self.listen

        Controls: When HSK_points meet a certain treshold, a fraction of the HSK characters remaining in the level
        will be added. At 70 points, all characters should be in the self.list.
        """
        for x in range(len(self.HSk_points)):
            hsk_level = x+1
            if self.HSk_points[x] >= self.HSK_thresholds[x]:
                string = f'hsk{hsk_level}_vocab'
                local_hsk_list = getattr(hr, string)
                char_to_add = []
                for i in range(int(len(local_hsk_list) * .08)):
                    char_list_difference = list(set(local_hsk_list) - set(self.list))
                    # Characters in current HSK level but not in list.
                    if len(char_list_difference) != 0:
                        char_to_add.append(char_list_difference[random.randint(0, (len(char_list_difference)) - 1)])
                self.list.append(char_to_add)
                aux.check_if_characters_in_repository(char_to_add)
                self.HSK_thresholds[x] += 5

    def check_if_profile_exists(self):
        return bool(os.path.exists(f'player_profiles\\{self.profile_name}'))

    def make_profile_folder(self):
        old_directory = os.getcwd()
        os.chdir('player_profiles')
        os.mkdir(self.profile_name)
        os.chdir(old_directory)

    def create_profile(self):
        profile_dict = dict()
        profile_dict['Name'] = self.profile_name
        profile_dict['titles'] = ['Initiate']
        profile_dict['Join Date'] = datetime.strftime(datetime.now(), "%m/%d/%Y")
        profile_dict['Profile age'] = None
        profile_dict['HSK_Level'] = 0
        HSK_dict = dict()
        HSK_dict['HSK Level'] = 0
        HSK_dict['HSK1 Points'] = 0
        HSK_dict['HSK2 Points'] = 0
        HSK_dict['HSK3 Points'] = 0
        HSK_dict['HSK4 Points'] = 0
        HSK_dict['HSK5 Points'] = 0
        HSK_dict['HSK6 Points'] = 0
        HSK_dict['HSK1 Threshold'] = 0
        HSK_dict['HSK2 Threshold'] = 5
        HSK_dict['HSK3 Threshold'] = 5
        HSK_dict['HSK4 Threshold'] = 5
        HSK_dict['HSK5 Threshold'] = 5
        HSK_dict['HSK6 Threshold'] = 5
        dr.profile_dictionary = profile_dict
        dr.HSK_dictionary = HSK_dict
        dr.profile_dictionary = profile_dict




    def instantiate_character_list(self):
        character_list = [i['Name'] for i in dr.character_dictionary]
        # if len(self.list_appends) > 0:
        #    list.append(self.list_appends)
        # **self.list_appends is not recognized**
        return character_list

    def fetch_csv_to_dict(self):
        old_dir = os.getcwd()
        os.chdir(f'player_profiles\\{self.profile_name}')
        with open(f'{self.profile_name}_Character_Data.csv', 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            new_dict = [dict(x) for x in reader]
            for x in new_dict:
                for k, v in x.items:
                    if k != 'Name' or 'HSK_Level':
                        x[k] = float(v)
                dr.character_dictionary = new_dict
        with open(f'{self.profile_name}_HSK_Data.csv', 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            new_dict = [dict(x) for x in reader]
            dr.HSK_dictionary = new_dict[0]
        with open(f'{self.profile_name}_Profile_Data.csv', 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            new_dict = [dict(x) for x in reader]
            dr.profile_dictionary = new_dict[0]
        os.chdir(old_dir)

    def save_files(self):
        old_dir = os.getcwd()
        os.chdir(f'player_profiles\\{self.profile_name}')

        with (open(f'{self.profile_name}_Profile_Data.csv', 'w+', newline='', encoding='utf-8')) as file:
            writer = csv.DictWriter(file, fieldnames=dr.profile_dictionary.keys())
            writer.writeheader()
            writer.writerow(dr.profile_dictionary)
        with (open(f'{self.profile_name}_HSK_Data.csv', 'w+', newline='', encoding='utf-8')) as file:
            writer = csv.DictWriter(file, fieldnames=dr.HSK_dictionary.keys())
            writer.writeheader()
            writer.writerow(dr.HSK_dictionary)
        with (open(f'{self.profile_name}_Character_Data.csv', 'w+', newline='', encoding='utf-8')) as file:
            writer = csv.DictWriter(file, fieldnames=dr.character_dictionary[0].keys())
            writer.writeheader()
            for i in dr.character_dictionary:
                writer.writerow(i)
        os.chdir(old_dir)

    def adjust_hsk_points(self, char, adjustment):
        level = aux.test_hsk_level(char)
        dr.HSK_dictionary[f'HSK{level} Points'] += float(adjustment)

    def calculate_hsk_points(self):
        (dr.HSK_dictionary['HSK1 Points'], dr.HSK_dictionary['HSK2 Points'], dr.HSK_dictionary['HSK3 Points'],
         dr.HSK_dictionary['HSK4 Points'], dr.HSK_dictionary['HSK5 Points'], dr.HSK_dictionary['HSK6 Points']) \
            = 0, 0, 0, 0, 0, 0
        for i in dr.character_dictionary:
            if i['HSK_Level'] == 1:
                dr.HSK_dictionary['HSK1 Points'] += float(i['Accuracy'])/len(hr.hsk1_vocab)
            elif i['HSK_Level'] == 2:
                dr.HSK_dictionary['HSK2 Points'] += float(i['Accuracy'])/len(hr.hsk2_new)
            elif i['HSK_Level'] == 3:
                dr.HSK_dictionary['HSK3 Points'] += float(i['Accuracy'])/len(hr.hsk3_new)
            elif i['HSK_Level'] == 4:
                dr.HSK_dictionary['HSK4 Points'] += float(i['Accuracy'])/len(hr.hsk4_new)
            elif i['HSK_Level'] == 5:
                dr.HSK_dictionary['HSK5 Points'] += float(i['Accuracy'])/len(hr.hsk5_new)
            elif i['HSK_Level'] == 6:
                dr.HSK_dictionary['HSK6 Points'] += float(i['Accuracy'])/len(hr.hsk6_new)


sign_in_input = input('\n\nPlease enter your profile name. If you enter an new name, a new profile will be created.')
# vocab_input= input('''Enter the list of chinese characters or phrases you would like to practice.
# you are advised to ensure your units of language are separate and do not constitute
# larger phrases than intended''')
select_mode = '\nFor now, only Adventure mode is enabled.'

# vi = qf.QuizList(vocab_input, sign_in_input, int(select_quiz_size))
game_object = ProfileObject(sign_in_input)
