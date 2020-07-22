# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:44:42 2020

@author: cruise
"""


class Calculator(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return(self.a + self.b)
    
    def subtract(self):
        return(self.a - self.b)
    
    def multiply(self):
        return(self.a * self.b)
    
    def divide(self):
        return(self.a / self.b)
    
    def exponent(self):
        return(self.a ** self.b)
    
    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b    

    def getA(self):
        return(self.a)
        
    def getB(self):
        return(self.b)
    
    def printAll(self):
        print(f"""Sum is: {self.add()} """)
    
        print(f"""Difference is: {self.subtract()} """)
    
        print(f"""Product is: {self.multiply()} """)
    
        print(f"""Division is: {self.divide()} """)
    
        print(f"""Power is: {self.exponent()} """)
    
        print(f"""A is: {self.getA()} """)
        
        print(f"""B is: {calc.getB()} """)
    
    
if __name__ == '__main__':
    calc = Calculator(5, 7)    
    calc.printAll()           
    calc.setA(0)    
    print('\nSetting A = 0.....')
    calc.printAll()       
    calc.setB(3)    
    print('\nSetting B = 3.....')
    calc.printAll()       
        
    