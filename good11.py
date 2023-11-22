from turtle import *

import turtle
wn= turtle.Screen()
wn.setup(width=400,height=400)
wn. bgcolor("blue")
wn. title("Heart!")

color("red")
begin_fill()
left(50)
forward(100)
circle(40,180)

left(260)
circle(40,180)
forward(100)
end_fill()
left(140)
color("red")
forward(100)
turtle.pencolor("white")
turtle.write("I LOVE YOU")
done()