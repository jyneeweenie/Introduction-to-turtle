import turtle
turtle.Screen().bgcolor("Red")
board = turtle.Turtle()
# creating a rectangle
for i in range(4):
    board.forward(180)
    board.right(90)
    i = i+1
# creating an equatorial triangle
board.forward(100) # draw base
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)
# creating a hexagon
for i in range(6):
    board.forward(100) 
    board.right(90)
    i = i+2

