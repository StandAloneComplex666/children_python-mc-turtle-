import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# Ask the user for the number of sides, default to 4, min 2, max 6
sides = int(turtle.numinput(4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# Our outer spiral loop
for m in range(100):
    for m2 in range(sides):
        t.penup()
        t.forward(m*4)
        t.pendown()
        # Our "inner" spiral loop
        # Draws a little spiral at each corner of the big spiral
        for n in range(5):
            t.pencolor(colors[n%5])
            t.circle(m)
            t.left(72)
        t.left(360/sides + 2) # Aim at the next point on the big spiral
