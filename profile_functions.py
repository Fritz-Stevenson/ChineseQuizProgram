import os, csv, random
import dictionary_repository as dr
from datetime import datetime
import hsk_repository as hr


class ProfileObject:
    def __init__(self, profile_name):
        self.list = []
        self.profile_name = profile_name
        if self.check_if_profile_exists() == False:
            self.make_profile_folder()
            self.create_profile()
        else:
            self.fetch_csv_to_dict()
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

    def check_to_add_characters(self):
        for x in range(len(self.HSk_points)):
            HSK_level = x+1
            if self.HSk_points[x] > self.HSK_thresholds[x]:
                string = f'hsk{HSK_level}_vocab'
                local_HSK_list = getattr(hr, string)
                for i in range(int(len(local_HSK_list) * .08)):
                    char_list_difference = list(set(local_HSK_list) - set(self.list))
                    if len(char_list_difference) != 0:
                        self.list.append(char_list_difference[random.randint(0, (len(char_list_difference)) - 1)])

    def check_if_profile_exists(self):
        return bool(os.path.exists(f'player_profiles\\{self.profile_name}'))

    def make_profile_folder(self):
        old_directory = os.getcwd()
        os.chdir('player_profiles')
        os.mkdir(self.profile_name)
        os.chdir(old_directory)

    def create_profile(self):
        profile_dict = {}
        profile_dict['Name'] = self.profile_name
        profile_dict['titles'] = ['Initiate']
        profile_dict['Join Date'] = datetime.strftime(datetime.now(), "%m/%d/%Y")
        profile_dict['Profile age'] = None
        profile_dict['HSK_Level'] = 0
        HSK_dict = {}
        HSK_dict['HSK Level'] = 0
        HSK_dict['HSK1 Points'] = 0
        HSK_dict['HSK2 Points'] = 0
        HSK_dict['HSK3 Points'] = 0
        HSK_dict['HSK4 Points'] = 0
        HSK_dict['HSK5 Points'] = 0
        HSK_dict['HSK6 Points'] = 0
        HSK_dict['HSK1 Threshold'] = 5
        HSK_dict['HSK2 Threshold'] = 5
        HSK_dict['HSK3 Threshold'] = 5
        HSK_dict['HSK4 Threshold'] = 5
        HSK_dict['HSK5 Threshold'] = 5
        HSK_dict['HSK6 Threshold'] = 5
        dr.profile_dictionary = profile_dict
        dr.HSK_dictionary = HSK_dict
        dr.profile_dictionary = profile_dict

    def test_HSK_level(self, char):
        if char in ''.join(hr.hsk1_vocab) and char not in ''.join(hr.hsk2_vocab):
            return 1
        elif char in ''.join(hr.hsk2_vocab) and char not in ''.join(hr.hsk3_vocab):
            return 2
        elif char in ''.join(hr.hsk3_vocab) and char not in ''.join(hr.hsk4_vocab):
            return 3
        elif char in ''.join(hr.hsk4_vocab) and char not in ''.join(hr.hsk5_vocab):
            return 4
        elif char in ''.join(hr.hsk5_vocab) and char not in ''.join(hr.hsk6_vocab):
            return 5
        elif char in ''.join(hr.hsk6_vocab):
            return 6
        else:
            return 0

    def check_if_characters_in_repository(self):
        for i in self.list:
            if not any(d['Name'] == i for d in dr.character_dictionary):
                char_dict = {}
                char_dict['Name'] = i
                char_dict['Accuracy'] = 0
                char_dict['HSK_Level'] = self.test_HSK_level(i)
                char_dict['Weight'] = 0
                dr.character_dictionary.append(char_dict)
        # No implementation of this yet

    def create_run_dict(self):
        pass

    def fetch_csv_to_dict(self):
        old_dir = os.getcwd()
        os.chdir(f'player_profiles\\{self.profile_name}')
        with open(f'{self.profile_name}_Character_Data.csv', 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            new_dict = [dict(x) for x in reader]
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

    def calculate_HSK_points(self):
        (dr.HSK_dictionary['HSK1 Points'],dr.HSK_dictionary['HSK2 Points'],dr.HSK_dictionary['HSK3 Points'],
        dr.HSK_dictionary['HSK4 Points'],dr.HSK_dictionary['HSK5 Points'],dr.HSK_dictionary['HSK6 Points']) =0
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
v = ProfileObject('Fritz')
v.save_files()