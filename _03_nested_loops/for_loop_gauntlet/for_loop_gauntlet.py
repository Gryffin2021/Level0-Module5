"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':

    #Single For-Loops

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

    #Nested For-Loops

    #1
    for i in range(3):
        for j in range(3):
            print(str(i) + str(j))
    #2
    for i in range(3):
        for j in range(3):
            print(str(3*i+j+1),end='')
        print()
    #3
    for i in range(10):
        for j in range(10):
            print(str(10*i+j+1),end='')
        print()
    #4
    for i in range(6):
        for j in range(i+1):
            print("* ", end='')
        print()

