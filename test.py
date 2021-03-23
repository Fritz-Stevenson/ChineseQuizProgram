series = 20
eq = lambda x,y: 1-((1-x)/1.25) if y == True else x/(1+.6*x)
x = .25
for i in range(series):
    y = True
    x = eq(x,y)
    print(x)

