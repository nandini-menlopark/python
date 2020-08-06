# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:20:14 2020

@author: cruise
"""


class ExpressionSolver(object):
    def __init__(self):
        self.a  = 0
        self.b = 0
                
    def getA(self):
        return(self.a)
    
    def getB(self):
        return(self.b)
    
    def getOperation(self):
        return(self.op)
    
    def getResult(self):
        if(self.op == '+'):
            return(self.a + self.b)
        
        if(self.op == '-'):
            return(self.a - self.b)
        
        if(self.op == '*'):
            return(self.a * self.b)
        
        if(self.op == '/'):
            return(self.a / self.b)
        
        if(self.op == '%'):
            return(self.a % self.b)
        
        if(self.op == '>'):
            return(self.a > self.b)

        if(self.op == '<'):
            return(self.a < self.b)
        
        if(self.op == '**'):
            return(self.a ** self.b)

        if(self.op == '=='):
            return(self.a == self.b)
        
        if(self.op == '!='):
            return(self.a != self.b)
        
        if(self.op == '>='):
            return(self.a >= self.b)
        
        if(self.op == '<='):
            return(self.a <= self.b)
        
        
    def solveExpression(self, expr):
        self.expr = expr.replace(' ', '')
        i = 0
        while(True):
            if self.expr[i].isnumeric() == False and self.expr[i] != '.':
                self.op = self.expr[i]
                if(self.expr[i+1].isnumeric() == False):
                    self.op = self.expr[(i):(i+2)]
                break
            i = i + 1
        mysplit = self.expr.split(self.op)
        self.a = float(mysplit[0])
        self.b = float(mysplit[1])
        return(self.getResult())
                

if __name__ == '__main__':
    
    myExprSolver = ExpressionSolver()
    
    expr = '500 == 200'
    
    print(f'Answer is {myExprSolver.solveExpression(expr)}')
    
