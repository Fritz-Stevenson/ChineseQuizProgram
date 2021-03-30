from chinese import ChineseAnalyzer
import random
import os
import hsk_repository as hr
import dictionary_repository as dr
from datetime import datetime
import profile_functions as pf
analyzer = ChineseAnalyzer()


class QuizList:
    def __init__(self, li, profile, question_count):
        self.profile = profile
        self.pf_object = pf.ProfileObject(profile)
        self.list = hr.hsk1_vocab #self.decide_hsk()
        self.list_length = len(li)
        self.analyzer =ChineseAnalyzer()
        for i in range(question_count):
            self.serve_question()

    def serve_question(self):
        char = self.list[random.randint(0,len(self.list))]
        zh_object = self.analyzer.parse(char)
        token = zh_object.tokens()[0]
        definition = zh_object[token[0]][0].definitions
        pinyin = zh_object[token[0]][0].pinyin
        approach = self.approach_roll()
        answer_bool = None
        #if approach == 0:
            #answer = input(f'What is the meaning of {token}')
            #if answer in definition:
            #    print ('True')
            #    answer_served = True
            #else:
            #    print('False')
            #    answer_served = False
        #if approach == 1:
            #answer = input(f'How would you pronounce {token} in pinyin?:  ')
            #if answer == ''.join(pinyin).lower():
            #    print('True')
            #    answer_served = True
            #else:
            #    print('False')
            #    answer_served = False
        #if approach == 2:
            #answer = input(f'What character(s) mean ({definition})?:  ')
            #if answer == token:
            #    print('True')
            #    answer_served = True
            #else:
            #    print('False')
            #    answer_served = False
        #if approach ==3:
        print(f'Entering a special round! Your character is {token}\n')
        answer= input('Enter a definition, the correct pinyin and tone, or ') # create another option for the answers
        self.assign_calculated_adjustments(token, answer_bool)
        self.pf_object.check_to_add_characters()
        print(token, pinyin, definition)

    def serve_question_easy(self):
        pass

    def approach_roll(self):
        approach = random.randint(0,3)
        return approach

    def create_word_list(self):
        pass

    def check_for_quit(self, user_input):
        if user_input.upper() != 'QUIT':
            return True
        else:
            pf.ProfileObject.save_files() # pf is a placeholder in this code

    def log_progress(self):
        self.pf_object.save_files()

    def assign_calculated_adjustments(self, character, value):
        eq = lambda x, y: x + (1 - x) * .25 if y == True else x - (x / 4)

        character_dict = next((i for i in dr.character_dictionary if i['Name'] == character), None)
        previous_accuracy = character_dict['Accuracy']
        character_dict['Accuracy'] = eq(previous_accuracy, value)
        adjustment_value = character_dict['Accuracy']-previous_accuracy
        self.adjust_HSK_Points(character, adjustment_value)


    def adjust_HSK_Points(self, char, adjustment):
        level = self.pf_object.test_HSK_level(char)
        dr.HSK_dictionary[f'HSK{level} Points'] += float(adjustment)






