#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

class Calculator(object):

    def add(self, a, b): #addition function
            return map(lambda x, y: x+y, a, b)

#    def add_alternative(a)
#            return reduce(lambda x,y: x+y, a)

    def subtract(self, a, b): #subtraction function
            return map(lambda x, y: x-y, a, b)
            
    def multiply(self, a, b): #multiplication function
            return map(lambda x, y: float(x*y), a, b)
            
    def divide(self, a, b): #division function
            return map(lambda x, y: float(x/y), a, b)
            
    def exponential(self, a, b): #exponential function
#        return a**b
            return map(lambda x, y: x**y, a, b)
    
    def square_root(self, a): #square root function
            return map(lambda x: x**0.5, a)

    def cube(self, a): #cube function
            return map(lambda x: x**3, a)
        
    def square(self, a): #square function
            return map(lambda x: x**2, a)
        
    def ten_power(self, a): #ten to the power x function
            return map(lambda x: 10**x, a)

    def inverse_function(self, a): #inverse function: y = 1/x
            return map(lambda x: 1/x, a)


print ('Results below:')
print ('Addition:'), add([10, 20, 30], [1, 2, 3]) 
print ('Subtraction:'), subtract([10, 20, 30], [1, 2, 3]) 
print ('Multiplication:'),multiply([10, 20, 30], [1, 2, 3])
print ('Division:'),divide([10, 20, 30], [1, 2, 3])
print ('Exponential:'),exponential([10, 20, 30], [1, 2, 3])
print ('Square root of: 5, 6, 7 ='),square_root([5, 6, 7])
print ('Cubed 5, 6, 7:'),cube([5, 6, 7])
print ('Squared 5, 6, 7:'),square([5, 6, 7])
print ('Ten to the power 3, 4, 5 :'),ten_power([3, 4, 5])
print ('Inverse function :'), ([4, 5, 8])
