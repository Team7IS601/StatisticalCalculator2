from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Stats.Mean import mean


def median(num):
    sortedNums = num.sorted()
    length = len(num)
    result = None
    index1 = division(length, 2)
    if length % 2 == 0:
        index2 = subtraction(index1, 1)
        value1 = sortedNums[index1]
        value2 = sortedNums[index2]
        result = mean([value1,value2])
    else:
        result = sortedNums[index1]
    return result