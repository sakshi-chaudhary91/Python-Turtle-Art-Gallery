import turtle

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "purple"]

for i in range(100):
    t.pencolor(colors[i % 6])
    t.forward(i * 3)
    t.left(121)

t.hideturtle()
turtle.done()