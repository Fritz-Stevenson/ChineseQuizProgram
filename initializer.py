import profile_functions as pf
import hsk_repository as hr
print('''Welcome to A Journey Eastward
A Chinese language code project by Fritz Stevenson
You will input a list of characters or phrases, 
select the size of the quiz, then answer a variety
of randomized questions regarding the entered vocabulary.''')

sign_in_input = input('\n\nPlease enter your profile name. If you enter an new name, we will create a profile for you. ')
#vocab_input= input('''Enter the list of chinese characters or phrases you would like to practice.
#you are advised to ensure your units of language are separate and do not constitute
#larger phrases than intended''')
select_mode = 'For now, only Adventure mode is enabled.'

#vi = qf.QuizList(vocab_input, sign_in_input, int(select_quiz_size))
vi = pf.ProfileObject(sign_in_input)
vi


'''Bug Log
currently feeding characters that are not in the dictionary

chinese api has unrecognized characters: 对，

ProfileObject.list_append is not recognized'''

'''Change Plans
--Need two different entry systems: one as a solid text block and one as the hsk_vocab list format. Also need a function 
to clean unnecessary special characters and letters from input.
'''