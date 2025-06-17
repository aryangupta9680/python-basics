import turtle

t = turtle.Turtle()
t.speed(2)
t.penup()

x = -50
y = 100
t.goto(x, y)

number = 8
for i in range(1, 11):
    t.goto(x, y - (i - 1) * 30)  # move down each row
    text = f"{number} x {i} = {number * i}"
    t.write(text, align="left", font=("Arial", 16, "normal"))

t.hideturtle()
turtle.done()