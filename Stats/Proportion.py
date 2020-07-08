from Calculator.Division import division
from Calculator.Addition import addition

def proportion(num):
    sum = 0
    for n in num:
        sum = addition(sum, n)

    result = []

    for n in num:
        value = division(n, sum)
        result.append(value)

    return result