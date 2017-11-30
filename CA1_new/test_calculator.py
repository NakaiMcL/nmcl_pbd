#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    
    def test_calculator_add(self): #tests the add functionality eg 5+5 = 10
        result = Calculator().add(5, 5)
        self.assertEqual(10, result)
        result = Calculator().add(2, 2)
        self.assertEqual(4, result)
        result = Calculator().add(2, 0)
        self.assertEqual(2, result)        
        result = Calculator().add(34, 6)
        self.assertEqual(40, result)

    def test_calculator_multiply(self): #tests the divide functionality eg 5*5 = 25
        result = Calculator().multiply(5, 5)
        self.assertEqual(25, result)
        result = Calculator().multiply(5, 2)
        self.assertEqual(10, result)
        result = Calculator().multiply(5, 0)
        self.assertEqual(0, result)        
        result = Calculator().multiply(3, 5)
        self.assertEqual(15, result)

    def test_calculator_divide(self): #tests the divide functionality eg 5/5 = 0
        result = Calculator().divide(5, 5)
        self.assertEqual(1, result)
        result = Calculator().divide(5, 1)
        self.assertEqual(5, result)
        result = Calculator().divide(5, 0.2)
        self.assertEqual(25, result)        
        result = Calculator().divide(5, 4)
        self.assertEqual(1.25, result)

    def test_calculator_subtract(self): #tests the subtract functionality eg 5-5 = 0
        result = Calculator().subtract(5, 5)
        self.assertEqual(0, result)
        result = Calculator().subtract(5, 2)
        self.assertEqual(3, result)
        result = Calculator().subtract(2, 0)
        self.assertEqual(2, result)        
        result = Calculator().subtract(3, 5)
        self.assertEqual(-2, result)
    
    def test_calculator_exponential(self): #tests the exponential functionality eg 5**2 = 25 
        result = Calculator().exponential(5, 2)
        self.assertEqual(25, result)
        result = Calculator().exponential(5, 4)
        self.assertEqual(625, result)
        result = Calculator().exponential(2, 2)
        self.assertEqual(4, result)        
        result = Calculator().exponential(2, 3)
        self.assertEqual(8, result)

    def test_calculator_square_root(self): #tests the square root functionality eg square root of 25 is 5 
        result = Calculator().square_root(25, 0.5)
        self.assertEqual(5, result)
        result = Calculator().square_root(81, 0.5)
        self.assertEqual(9, result)
        result = Calculator().square_root(36, 0.5)
        self.assertEqual(6, result)        
        result = Calculator().square_root(144, 0.5)
        self.assertEqual(12, result)

    def test_calculator_cube(self): #tests the cube functionality eg 3 cubed is 27 
        result = Calculator().cube(3, 3)
        self.assertEqual(27, result)
        result = Calculator().cube(2, 3)
        self.assertEqual(8, result)
        result = Calculator().cube(5, 3)
        self.assertEqual(125, result)        
        result = Calculator().cube(12, 3)
        self.assertEqual(1728, result)

    def test_calculator_square(self): #tests the square functionality eg 3 squared is 9 
        result = Calculator().square(3, 2)
        self.assertEqual(9, result)
        result = Calculator().square(7, 2)
        self.assertEqual(49, result)
        result = Calculator().square(8, 2)
        self.assertEqual(64, result)        
        result = Calculator().square(13, 2)
        self.assertEqual(169, result)

    def test_calculator_ten_to_the_power(self): #tests the ten to the power functionality eg 10 to the power 2 is 100 
        result = Calculator().ten_to_the_power(2, 10)
        self.assertEqual(100, result)
        result = Calculator().ten_to_the_power(3, 10)
        self.assertEqual(1000, result)
        result = Calculator().ten_to_the_power(4, 10)
        self.assertEqual(10000, result)        
        result = Calculator().ten_to_the_power(5, 10)
        self.assertEqual(100000, result)

    def test_calculator_inverse_function(self): #tests the ten to the power functionality eg 10 to the power 2 is 100 
        result = Calculator().inverse_function(2)
        self.assertEqual(0.5, result)
        result = Calculator().inverse_function(5)
        self.assertEqual(0.2, result)
        result = Calculator().inverse_function(10)
        self.assertEqual(0.1, result)        
        result = Calculator().inverse_function(100)
        self.assertEqual(0.01, result)
    
if __name__ == '__main__':
    unittest.main()
