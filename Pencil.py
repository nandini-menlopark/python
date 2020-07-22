# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:02:12 2020

@author: cruise
"""
from termcolor import colored
import string
import numpy as np

class Pencil(object):
    def __init__(self, color):
        self.color = color
    
    def checkColor(self):
        print(colored(f"""I am a {self.color} pencil""", self.color))
        
    def write(self, text):
        return(colored(text, self.color))
    
    def writeAlphabets(self):
        return(colored(string.ascii_lowercase, self.color))
    
    def writeNumerals(self):
        return(colored(np.arange(0,11), self.color))
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return(self.color)
       
if __name__ == "__main__":
    
    myPencil = Pencil('cyan')
    myPencil.checkColor()    
    print(myPencil.write('I am a nice python programmer, python is a cool language'))
   
    print(myPencil.writeAlphabets())

   
    print(myPencil.writeNumerals())
    
    
    # Pencil('red').checkColor()
    # Pencil('green').checkColor()
    # Pencil('yellow').checkColor()
    # Pencil('blue').checkColor()
    # Pencil('red').checkColor()
    # Pencil('magenta').checkColor()
    # Pencil('cyan').checkColor()
    # Pencil('white').checkColor()
    
    
    myPencil.getColor()
    
    myPencil.setColor('blue')
    myPencil.getColor()
    myPencil.checkColor()    
