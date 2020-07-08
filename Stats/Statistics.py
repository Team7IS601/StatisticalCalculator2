from Calculator.Calculator import Calculator
from Stats.Mean import mean
from Stats.Median import median
from Stats.Mode import mode
from Stats.Proportion import proportion
from Stats.StandardDeviation import standardDev
from Stats.CorrelationCoefficient import correlation
from Stats.ZScore import zscore

class Statistics(Calculator):
    data = []

    def __int__(self):
        super().__int__()


    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standardDev(self, data):
        self.result = standardDev(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def correlation_coefficient(self, data, data1):
        self.result = correlation(data, data1)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    def p_value(self, data):
        self.result = pvalue(data)
        return self.result