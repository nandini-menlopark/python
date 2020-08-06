import turtle
import random
import numpy as np

stamp = turtle.Turtle()

stamp.shape('turtle')

stamp.penup()


turtle.colormode(255)


paces = 30

random_red = 50

random_green = 50

random_blue = 50


for i in np.arange(150):
        random_red = random.randint(0, 255)
        random_green = random.randint(0, 255)
        random_blue = random.randint(0, 255)
        
        stamp.color(random_red, random_green, random_blue)
        
        stamp.stamp()
        
        paces += 5
        
        stamp.forward(paces)
        
        stamp.right(20)
        

turtle.clear()
