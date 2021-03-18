import re
from chinese import ChineseAnalyzer
import hsk_repository
import test_insert

analyzer = ChineseAnalyzer()

inp= test_insert.insert1
hsk_new_list= []
regex = re.findall(r'([\u4e00-\u9fff]+)', inp)
def f(x, y):
    result = set(y)-set(x)
    return list(result)
difference = f(hsk_repository.hsk5_vocab, hsk_repository.hsk6_vocab)
print(difference)
print(len(difference))

#print(regex)
#print(len(regex))
