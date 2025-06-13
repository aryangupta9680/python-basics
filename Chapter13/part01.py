import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create a turtle object
pen = turtle.Turtle()
pen.color("blue")         # Set the color of the pen
pen.pensize(3)            # Set the thickness of the pen

# Use a for loop to draw a square
for _ in range(4):
    pen.forward(100)      # Move forward by 100 units
    pen.left(90)          # Turn left by 90 degrees

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()