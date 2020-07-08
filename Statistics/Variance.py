from Calculator.Square import square
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Stats.Mean import mean

def variance(num):
    mean = mean(num)
    total = 0
    for n in num:
        difference = subtraction(n, mean)
        square = square(difference)
        total = addition(total, square)
    result = division(total, len(num))
    return result