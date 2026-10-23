import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(180):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i * 1.5)
    t.left(59)

turtle.done()