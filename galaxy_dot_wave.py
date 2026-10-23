import turtle
import math

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["#00FFFF", "#FF69B4", "#ADFF2F", "#FF4500"]

for i in range(180):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 2)
    t.forward(120)
    t.pendown()
    t.pencolor(colors[i % len(colors)])
    t.dot(10 + (i % 5))

turtle.done()