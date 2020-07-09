from Calculator.Squareroot import sqrt
from Stats.Variance import variance

def standardDev(data):
    var = variance(data)
    return round(sqrt(var), 2)