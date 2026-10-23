import turtle

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["#FF1493", "#00FFFF", "#FFD700", "#39FF14", "#9370DB"]

for i in range(120):
    t.pencolor(colors[i % len(colors)])
    t.circle(100)
    t.left(3)

t.hideturtle()
turtle.done()