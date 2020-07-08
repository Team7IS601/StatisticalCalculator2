from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Square import square
from Calculator.Squareroot import sqrt

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        ##Addition Function##
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        ##Subtract Function##
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        ##Multiply Function##
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        ##Divide Function##
        self.result = division(a, b)
        return self.result

    def square(self, a):
        ##Square Function##
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        ##Square Root Function##
        self.result = sqrt(a)
        return self.result