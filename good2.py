import turtle
window = turtle.Screen()
turtle.speed(10)
for i in range(30):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()