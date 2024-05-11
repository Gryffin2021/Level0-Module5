"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import random

def draw_house(height):
    if height == 'medium':
        height1 = 120
    elif height == 'large':
        height1 = 250
    else:
        height1 = 60
    timmy.left(90)
    timmy.forward(height1)
    timmy.right(90)
    timmy.forward(35)
    timmy.right(90)
    timmy.forward(height1)
    timmy.left(90)
    timmy.pencolor('LIME')
    timmy.forward(50)
    timmy.pencolor('BLACK')

def draw_pointy_roof(height):
    if height == 'medium':
        height1 = 120
    else:
        height1 = 60
    timmy.left(90)
    timmy.forward(height1)
    timmy.right(45)
    timmy.forward(17.5)
    timmy.right(90)
    timmy.forward(17.5)
    timmy.right(45)
    timmy.forward(height1)
    timmy.left(90)
    timmy.pencolor('LIME')
    timmy.forward(50)
    timmy.pencolor('BLACK')

def draw_flat_roof(height):
    if height == 'large':
        height1 = 250
    else:
        height1 = 10000
    timmy.left(90)
    timmy.forward(height1)
    timmy.right(90)
    timmy.forward(35)
    timmy.right(90)
    timmy.forward(height1)
    timmy.left(90)
    timmy.pencolor('LIME')
    timmy.forward(50)
    timmy.pencolor('BLACK')
if __name__ == '__main__':
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    timmy = turtle.Turtle()
    timmy.penup()
    timmy.setx(-400)
    timmy.sety(-350)
    timmy.pendown()
    ran = 0
    for i in range(9):
        ran = random.randint(0, 2)
        if ran == 1:
            var_type = 'medium'
        elif ran == 2:
            var_type = 'large'
        else:
            var_type = 'small'
        if var_type == 'large':
            draw_flat_roof(var_type)
        else:
            draw_pointy_roof(var_type)
    pass
