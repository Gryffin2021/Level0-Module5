"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    #1
    for i in range(101):
        print(i)
    #2
    j = 101
    for i in range(101):
        j -= 1
        print(j)
    #3
    for i in range(101):
        if i % 2 == 0:
            print(i)
    #4
    for i in range(100):
        if i % 2 == 1:
            print(i)
    #5
    for i in range(101):
        if i % 2 == 0:
            print(i, " is even")
        else:
            print(i, " is odd")
    #6
    for i in range(778):
        if i % 7 == 0:
            print(i)
    #7
    for i in range(14):
        year = i + 2010
        print("In ", year, ", I was ", i, " years old!")
    pass
