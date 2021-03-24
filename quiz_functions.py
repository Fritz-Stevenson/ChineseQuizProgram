from chinese import ChineseAnalyzer
import random
import os
import hsk_repository as hr
from datetime import datetime
analyzer = ChineseAnalyzer()
class QuizList:
    def __init__(self, li, profile, question_count):
        self.profile = profile
        self.list = hr.hsk1_vocab #self.decide_hsk()
        self.list_length = len(li)
        self.profile_dict ={}
        self.character_dict =[]
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
                char_dict['Accuracy'] = 0
                char_dict['HSK_Level'] = self.test_HSK_level(i)
                char_dict['Weight'] = 0
                self.dict.append(char_dict)
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
    def serve_question(self):
        char = self.list[random.randint(0,len(self.list))]
        zh_object = self.analyzer.parse(char)
        token = zh_object.tokens()[0]
        definition = zh_object[token[0]][0].definitions
        pinyin = zh_object[token[0]][0].pinyin
        approach = self.approach_roll()
        #if approach == 0:
            #answer = input(f'What is the meaning of {token}')
            #if answer in definition:
            #    print ('True')
            #else:
            #    print('False')
        #if approach == 1:
            #answer = input(f'How would you pronounce {token} in pinyin?:  ')
            #if answer == ''.join(pinyin).lower():
            #    print('True')
            #else:
            #    print('False')
        #if approach == 2:
        answer = input(f'What character(s) mean ({definition})?:  ')
        if answer == token:
            print('True')
        else:
            print('False')
        print(token, pinyin, definition)
    def approach_roll(self):
        approach = random.randint(0,3)
        return approach
    def create_word_list(self):
        pass
    def check_for_quit(self, user_input):
        if user_input.upper() != 'QUIT':
            return True
        else:
            pass
            #save dictionaries to csv
            #quit program
    def log_progress(self,):
        pass


