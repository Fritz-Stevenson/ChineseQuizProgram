from chinese import ChineseAnalyzer
import random
import dictionary_repository as dr
from datetime import datetime
import initializer as ini  # error here
analyzer = ChineseAnalyzer()


class QuizClass:
    """Class attribute which arbitrates questions and progress of the game

    Returns: Infinite strings of questions while quit_token is not raised

    """
    def __init__(self):
        self.list = ini.game_object.list
        self.list_length = len(self.list)
        self.analyzer = ChineseAnalyzer()
        self.quit_token = False
        while not self.quit_token:
            self.serve_question()

    def serve_question(self):
        """Administers a randomized question and calls check_for_quit and assign_calculated adjustments."""
        char = self.list[random.randint(0, len(self.list))]
        zh_object = self.analyzer.parse(char)
        token = zh_object.tokens()[0]
        definition = zh_object[token][0].definitions
        pinyin = zh_object[token][0].pinyin
        approach = self.approach_roll()
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
        self.check_for_quit(answer)
        self.assign_calculated_adjustments(token, answer_bool)
        ini.game_object.check_to_add_characters()
        print(token, pinyin, definition)

    def serve_question_easy(self):
        pass

    def approach_roll(self):
        """Randomizes question archetype for variability and skill building"""
        approach = random.randint(0, 3)
        return approach
    
    def check_for_quit(self, user_input):
        """Checks input for quit command
        
        Args: 
            user_input: Input to check for quit command.
        
        Returns: controls self.quit_token which controls the __init__ serve_question loop.
        """
        if user_input.upper() != 'QUIT':
            pass
        else:
            ini.game_object.save_files()  # pf is a placeholder in this code
            self.quit_token = True

    def assign_calculated_adjustments(self, character, value):
        """Adjusts the values in the dictionary_repository to reflect the answer given
        
        Args:
            character: The token used for the quiz question.
            value: The boolean value of the answer(True or False).     
        """
        
        eq = lambda x, y: x + (1 - x) * .25 if y else x - (x / 4)

        character_dict = [i for i in dr.character_dictionary if i['Name'] == character][0]
        previous_accuracy = character_dict['Accuracy']
        character_dict['Accuracy'] = eq(previous_accuracy, value)
        adjustment_value = character_dict['Accuracy']-previous_accuracy
        ini.game_object.adjust_HSK_Points(character, adjustment_value)
