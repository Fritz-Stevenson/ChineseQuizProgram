from chinese import ChineseAnalyzer
zh_list ='喂你好我是学生'
analyzer = ChineseAnalyzer()
final = analyzer.parse(zh_list)
a = final.tokens()[0]
result = final[a]
answer = result[0].definitions
print(result[0].definitions)
