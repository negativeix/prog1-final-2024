import turtle
import random

'''my turtle clear doesn't work as i think so number keep disappear imediatly
 if it work i will put this class combine with ball in the middle of white canvas

'''


class Digit:
    def __init__(self, my_turtle):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        my_turtle.color(255, 0, 0)
        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.goto(0, 0)
        my_turtle.pensize(10)
        self.digit = 0

    def draw(self, digit):
        self.digit = digit
        if self.digit == 0:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()

        if self.digit == 1:
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if self.digit == 2:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.penup()

        if self.digit == 3:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if self.digit == 4:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.penup()

        if self.digit == 5:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if self.digit == 6:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if self.digit == 7:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if self.digit == 8:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.penup()

        if self.digit == 9:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

    def clear(self, my_turtle):
        my_turtle.clear()

    def my_delay(self, dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass


my_turtle = turtle.Turtle()
x = Digit(my_turtle)
while True:
    n = random.randint(0, 9)
    print(n)
    x.draw(n)
    x.my_delay(0.2)
    my_turtle.clear()
    turtle.update()
turtle.done()