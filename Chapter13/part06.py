import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()

x = -100
y = 100
t.goto(x, y)  # Move pen to starting position

for i in range(1, 11):  # rows 1 to 10
    current_y = y - (i - 1) * 20
    t.goto(x, current_y)
    for j in range(1, 11):  # columns 1 to 10
        t.write(i * j, align="center", font=("Arial", 12, "normal"))
        t.forward(20)  # move right to next column

t.hideturtle()
turtle.done()