import turtle

row = 0
column = 0

while (row <= 5):
    turtle.penup()
    turtle.goto(0, column * 100)
    turtle.pendown()

    turtle.forward(500)

    row += 1
    column += 1

row = 0
column = 0

turtle.setheading(90)

while(row <= 5):
    turtle.penup()
    turtle.goto(row * 100, 0)
    turtle.pendown()

    turtle.forward(500)

    row += 1
    column += 1
