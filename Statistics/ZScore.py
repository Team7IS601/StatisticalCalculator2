from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Stats.StandardDeviation import standardDev
from Stats.Mean import mean

def zscore(num):
    m = mean(num)
    sd = standardDev(num)
    result = []
    for n in num:
        value = division(subtraction(n, m), sd)
        result.append(round(value, 6))
    return result
