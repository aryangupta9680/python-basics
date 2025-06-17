import turtle

# Create screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()


t.speed(1)
# Starting point
t.penup()
t.goto(-100, -50)  # Move to the first point without drawing
t.pendown()

# Draw triangle using goto
t.goto(0, 100)      # Move to the top vertex
t.goto(100, -50)    # Move to the bottom right vertex
t.goto(-100, -50)   # Move back to the starting point

# Hide turtle and display the window
t.hideturtle()
screen.mainloop()