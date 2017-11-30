#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

class Calculator(object):
    
    number_types = (int, float, complex)

    def add(self, x, y): #addition function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
    
    def subtract(self, x, y): #subtraction function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
            
    def multiply(self, x, y): #multiplication function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError  
            
    def divide(self, x, y): #division function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x / y
        else:
            raise ValueError
            
    def exponential(self, x, y): #exponential function
#        return x**y
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x**y
        else:
            raise ValueError
    
    def square_root(self, x, y): #square root function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x**y
        else:
            raise ValueError

    def cube(self, x, y): #cube function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and y == 3:
            return x**y
        else:
            raise ValueError

    def square(self, x, y): #square function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and y == 2:
            return x**y
        else:
            raise ValueError

    def ten_to_the_power(self, x, y): #ten to the power x function
        number_types = (int, float, complex)
        if isinstance(x, number_types) and y == 10:
            return y**x
        else:
            raise ValueError

    def inverse_function(self, x): #inverse function: y = 1/x
        number_types = (int, float, complex)
        if isinstance(x, number_types):
            return 1 / x
        else:
            raise ValueError


