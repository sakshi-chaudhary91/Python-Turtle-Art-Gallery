import turtle

# Screen aur turtle setup
s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
t.color("red")
t.fillcolor("red")
t.speed(3)

# Heart drawing logic
t.begin_fill()
t.left(140)
t.forward(113)
t.circle(-57, 200)
t.setheading(60)
t.circle(-57, 200)
t.forward(113)
t.end_fill()

t.hideturtle()
turtle.done()