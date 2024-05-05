"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def triangle():
    timmy.pendown()
    for i in range(3):
        timmy.forward(50)
        timmy.left(120)

def square():
    timmy.pendown()
    for i in range(4):
        timmy.forward(50)
        timmy.left(90)

def circle():
    timmy.pendown()
    for i in range(360):
        timmy.forward(2)
        timmy.left(1)

if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    timmy = turtle.Turtle()
    shape = simpledialog.askstring(title="Shape",prompt="Whould you like to draw a square, triangle, or circle?")
    if shape == "square":
        square()
    elif shape == "triangle":
        triangle()
    else:
        circle()
    pass
