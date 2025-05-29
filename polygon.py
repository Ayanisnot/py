import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup("300,400")

pen = turtle.turtle()


num_sides = 6
side_length = 70
angles = 360 // num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angles)

turtle.done()