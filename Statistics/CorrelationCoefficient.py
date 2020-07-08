from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Stats.Proportion import proportion
from Stats.Median import median
from Stats.Mode import mode
from Stats.StandardDeviation import standardDev
from Stats.ZScore import zscore
from Stats.Mean import mean
##from Stats.CorrelationCoefficient import correlation
from Stats.VarianceOfPopulationProportion import varianceOfProportion
from Stats.Variance import variance


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def stddev(self, data):
        self.result = standardDev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    # def correlation_coefficient(self, data, data1):
    #     self.result = correlation(data, data1)
    #     return self.result

    def population_proportion_variance(self, data):
        self.result = varianceOfProportion(data)
        return self.result

    # def confidence_interval_top(self, data):
    #     self.result = confidence_interval_top(data)
    #     return self.result
    #
    # def confidence_interval_bottom(self, data):
    #     self.result = confidence_interval_bottom(data)
    #     return self.result

    pass