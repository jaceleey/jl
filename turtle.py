import turtle
my_screen = turtle.Screen()
my_screen.bgcolor("light yellow")
my_screen.title("turtle class")
my_turtle= turtle.Turtle()
turtle.speed(1)
for i in range(3):
    for j in range(8):
        my_turtle.forward(100)
        my_turtle.backward(100)
        my_turtle.right(45)
