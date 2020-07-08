from Stats.Proportion import proportion
from Stats.Variance import variance

def varianceOfProportion(num):
    prop = proportion(num)
    result = variance(prop)
    return result