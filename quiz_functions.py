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

        for i in range(question_count):
            self.serve_question()


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


