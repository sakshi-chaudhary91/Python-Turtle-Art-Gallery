import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

t.speed(0)
t.color("red")


for i in range(120):
    t.circle(190 - i, 90)
    t.left(90)
    t.circle(190 - i, 90)
    t.left(30)

turtle.done()