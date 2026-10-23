import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

colors = ["#FF1493", "#00FFFF", "#FFD700", "#FF4500", "#9370DB"]

for i in range(150):
    t.pencolor(colors[i % 5])
    t.circle(i, 45)
    t.left(90)
    t.circle(i, 45)
    t.left(10)

turtle.done()