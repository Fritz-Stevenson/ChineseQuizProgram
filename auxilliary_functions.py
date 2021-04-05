import dictionary_repository as dr
import hsk_repository as hr


def calculated_adjustments(character, value):
    """Adjusts the values in the dictionary_repository to reflect the answer given

    Args:
        character: The token used for the quiz question.
        value: The boolean value of the answer(True or False).
    """
    # lambda function that changes accuracy rating of character.
    eq = lambda x, y: x + (1 - x) * .25 if y else x - (x / 4)
    # Adds or subtracts difference from 1 or zero, depending on True or False Value
    character_dict = [i for i in dr.character_dictionary if i['Name'] == character][0]
    previous_accuracy = float(character_dict['Accuracy'])
    print(type(previous_accuracy))
    character_dict['Accuracy'] = eq(previous_accuracy, value)
    adjustment_value = character_dict['Accuracy'] - previous_accuracy
    return adjustment_value
    # please add a weight adjustment based on boolean value!

def check_for_quit(user_input):
    """Checks input for quit command

    Args:
        user_input: Input to check for quit command.

    Returns: controls self.quit_token which controls the __init__ serve_question loop.
    """
    if user_input.upper() != 'QUIT':
        return False
    else:
        return True


def approach_roll():
    import random
    """Randomizes question archetype for variability and skill building"""
    approach = random.randint(0, 3)
    return approach


def test_hsk_level(char):
    """Tests the hsk_level of the character inputed

    Args:
        char = Chinese character or phrase to be tested

    Returns: The HSK Level of character.

    """
    if char in ''.join(hr.hsk1_vocab) and char not in ''.join(hr.hsk2_new):
        return 1
    elif char in ''.join(hr.hsk2_vocab) and char not in ''.join(hr.hsk3_new):
        return 2
    elif char in ''.join(hr.hsk3_vocab) and char not in ''.join(hr.hsk4_new):
        return 3
    elif char in ''.join(hr.hsk4_vocab) and char not in ''.join(hr.hsk5_new):
        return 4
    elif char in ''.join(hr.hsk5_vocab) and char not in ''.join(hr.hsk6_new):
        return 5
    elif char in ''.join(hr.hsk6_new):
        return 6
    else:
        return 7


def check_if_characters_in_repository(character_list):
    """Checks if a character is in the dictionary repository and appends the repository if needed.

    Args:
        character_list = The running list used by the ProfileObject instantiation
    Results:
        Appends the missing characters to the character dictionary in the dictionary repository.
    """
    for i in character_list:
        if not any(d['Name'] == i for d in dr.character_dictionary):
            char_dict = dict()
            char_dict['Name'] = i
            char_dict['Accuracy'] = 0
            char_dict['HSK_Level'] = test_hsk_level(i)
            char_dict['Weight'] = 0
            dr.character_dictionary.append(char_dict)
