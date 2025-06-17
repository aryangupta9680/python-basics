import turtle

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create turtle object
pen = turtle.Turtle()
pen.pensize(3)  # Set pen thickness
pen.color("blue")  # Set pen color

# Draw a circle
pen.circle(100)  # 100 is the radius of the circle

pen.hideturtle()
screen.exitonclick()