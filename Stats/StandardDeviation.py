from Calculator.Squareroot import sqrt
from Stats.Variance import variance

def standardDev(num):
    var = variance(num)
    squareRoot = sqrt(var)
    result = round(squareRoot, 2)
    return float(result)