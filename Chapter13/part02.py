import turtle

# Create turtle object
hex_turtle = turtle.Turtle()

# Set speed and color (optional)
hex_turtle.speed(2)
hex_turtle.pencolor("blue")

# Draw a hexagon using for loop
for _ in range(6):
    hex_turtle.forward(100)  # Move forward by 100 units
    hex_turtle.left(60)      # Turn left by 60 degrees


hex_turtle.hideturtle()
turtle.done()