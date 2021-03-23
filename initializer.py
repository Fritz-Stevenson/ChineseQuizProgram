import quiz_functions as qf
import hsk_repository as hr
print('''Welcome to Chinese Quiz Creator
A code project by Fritz Stevenson
You will input a list of characters or phrases, 
select the size of the quiz, then answer a variety
of randomized questions regarding the entered vocabulary.''')

sign_in_input = input('\n\nPlease enter your profile name. If you enter an new name, we will create a profile for you.')
vocab_input= input('''Enter the list of chinese characters or phrases you would like to practice.
you are advised to ensure your units of language are separate and do not constitute
larger phrases than intended''')
select_quiz_size = input('''What is the number of questions you would like to answer?
Input free run to climb the HSK rankings.'''
                         )
#vi = qf.QuizList(vocab_input, sign_in_input, int(select_quiz_size))
vi = qf.QuizList(''.join(hr.hsk1_vocab), fre, int(select_quiz_size))


'''Bug Log
The parser has made errors. If we can feed the chinese module words/phrases from the hsk lists directly as pre-parsed 
objects, we can bypass the large amount of error testing and data entry inherent in sorting out word lists.'''

'''Change Plans
--Need two different entry systems: one as a solid text block and one as the hsk_vocab list format. Also need a function 
to clean unnecessary special characters and letters from input.
'''