from chinese import ChineseAnalyzer
import random
import os
import hsk_repository as hr
analyzer = ChineseAnalyzer()
class QuizList:
    def __init__(self, li, profile, question_count):
        self.profile = profile
        self.list = analyzer.parse(li)
        self.list_length = len(li)
        self.dict =[]
        for i in range(question_count):
            self.serve_question()
    def check_profile_exists(self):
        dirlist = os.listdir('player_profiles')
        return True if self.profile in dirlist else False
    def create_profile(self):
        pass
    def create_run_dict(self):
        for i in self.list:
            self.dict['Name'] = self.profile
            self.dict['Accuracy'] = None
            self.dict['HSK_Level'] = self.test_HSK_level(i)
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
        print(definition)
        answer= input(f'What is the meaning of {char_id}')
