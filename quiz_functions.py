from chinese import ChineseAnalyzer
import random
import os
import hsk_repository as hr
from datetime import datetime
analyzer = ChineseAnalyzer()
class QuizList:
    def __init__(self, li, profile, question_count):
        self.profile = profile
        self.list = analyzer.parse(li)
        self.list_length = len(li)
        self.profile_dict ={}
        self.dict =[]
        for i in range(question_count):
            self.serve_question()
    def check_profile_exists(self):
        dirlist = os.listdir('player_profiles')
        return True if self.profile in dirlist else False
    def create_profile(self):
        profile_dict = {}
        profile_dict['Name'] = self.profile
        profile_dict['titles'] = ['Initiate']
        profile_dict['Join Date'] = datetime.strftime(datetime.now(), "%m/%d/%Y")
        profile_dict['Profile age'] = None
        HSK_dict = {}
        HSK_dict['HSK Level'] = 0
        HSK_dict['HSK1 Points'] = 0
        HSK_dict['HSK2 Points'] = 0
        HSK_dict['HSK3 Points'] = 0
        HSK_dict['HSK4 Points'] = 0
        HSK_dict['HSK5 Points'] = 0
        self.profile_dict.append(profile_dict)
        self.profile_dict.append(HSK_dict)
    def create_run_dict(self):
        for i in self.list:
            if not any(d['Name'] == i for d in self.dict):
                char_dict = {}
                char_dict['Name'] = i
                char_dict['Accuracy'] = None
                char_dict['HSK_Level'] = self.test_HSK_level(i)
                char_dict['Weight'] = 0
                self.dict.append(char_dict)
    def test_HSK_level(self, char):
        if char in hr.hsk1_vocab:
            return 1
        elif char in hr.hsk2_new:
            return 2
        elif char in hr.hsk3_new:
            return 3
        elif char in hr.hsk4_new:
            return 4
        elif char in hr.hsk5_new:
            return 5
        elif char in hr.hsk6_new:
            return 6
        else:
            return 0
    def serve_question(self):
        char_id = self.list.tokens()[random.randint(0,len(self.list))]
        zh_object = self.list[char_id]
        definition = zh_object[0].definitions
        pinyin = zh_object[0].pinyin
        approach = self.approach_roll()
        #if approach == 0:
            #answer = input(f'What is the meaning of {char_id}')
            #if answer in definition:
            #    print ('True')
            #else:
            #    print('False')
        #if approach == 1:
            #answer = input(f'How would you pronounce {char_id} in pinyin?:  ')
            #if answer == ''.join(pinyin).lower():
            #    print('True')
            #else:
            #    print('False')
        #if approach == 2:
        answer = input(f'What character(s) mean ({definition})?:  ')
        if answer == char_id:
            print('True')
        else:
            print('False')
        print(char_id, pinyin, definition)
    def approach_roll(self):
        approach = random.randint(0,3)
        return approach
    def check_for_quit(self, user_input):
        if user_input.upper() != 'QUIT':
            return True
        else:
            pass
            #save dictionaries to csv
            #quit program
    def log_progress(self,):
        pass


