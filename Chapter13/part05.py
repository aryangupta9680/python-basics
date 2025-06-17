import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle with Text")

# Create turtle object
t = turtle.Turtle()
t.speed(3)

# Draw filled circle with gray color
t.penup()
t.goto(0, -100)    # Move turtle to the bottom of the circle
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.circle(100)      # Draw circle with radius 100
t.end_fill()

# Move turtle to the center of the circle to write text
t.penup()
t.goto(0, -10)     # Slightly adjusted vertically for better centering
t.pendown()

# Write text inside the circle
t.color("black")
t.write("Circle!", align="center", font=("Arial", 24, "normal"))

# Hide turtle and finish
t.hideturtle()
screen.mainloop()