import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

colors = ["#39FF14", "#00FFFF", "#FF007F"]

for i in range(180):
    t.pencolor(colors[i % 3])
    t.forward(i * 2)
    t.left(145)

turtle.done()