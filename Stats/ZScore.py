from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Stats.StandardDeviation import standardDev
from Stats.Mean import mean

def zscore(num):
    Mean_var = mean(num)
    standardDev_var = standardDev(num)

    negative = []
    for Raw_var in num:
        meanRaw = subtraction(Mean_var, Raw_var)
        negative.append(meanRaw)

    ZScore_var = []
    for neg in negative:
        z = division(standardDev_var, neg)
        ZScore_var.append(z)

    return ZScore_var
