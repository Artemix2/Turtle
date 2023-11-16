from turtle import * # initialize all from turtle library ( * indicate all) 
import colorsys   # colorsys another library (it includes different colors)

speed(0)   # turtle speed
bgcolor('black')  # turtle background black (here you can change the color)
hue=0.0        # variable
hideturtle()   # hide turtle
pensize(2)   # size of turtle (change the value and try ) 

for i in range(185):   # its a loop provide obj range (change value and check )

    color=colorsys.hsv_to_rgb(hue,1,1)   # variable color, it stores colorsys properties 
    
    pencolor(color)  # turtle color, color variable includes property of colorsys 
    
    circle(190-i,90)  # turtle circle value (if you want change the value  and try)
    
    lt(90)         # turtle turn left direction
    
    circle(190-i,90)  
    
    lt(10)          # turtle turn left (change the value and try then you understand better)
    
    hue+=0.005  # (+=0.005) it make different colours in turtle  
    

done() # stop the turtle