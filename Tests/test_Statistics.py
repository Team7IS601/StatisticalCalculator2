import unittest
from pprint import pprint
from Stats.Statistics import Statistics
from CsvReader.CsvReader3 import getFileData


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.unit_test_statistics_answer = getFileData('Tests/Data/UnitTestStatisticsAnswers.csv').data
        self.test_data_mean = getFileData('Tests/Data/Test_Data_Mean.csv').data
        self.test_data_median = getFileData('Tests/Data/Test_Data_Median.csv').data
        self.unit_test_statistics = getFileData('Tests/Data/UnitTestStatistics.csv').data
        self.test_data_sample = getFileData('Tests/Data/TestDataSample.csv').data
        # self.column1 = [int(row['Value 1']) for row in self.test_data]
        # self.column2 = [int(row['Value 2']) for row in self.test_data]
        # self.test_zscore_answers = getFileData('Tests/Data/TestZScoresAnswers.csv').data
        # self.column_zscore = [float(row['Z-Score']) for row in self.zscoreanswers]


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        for row in self.test_data_mean:
            result = row["Mean"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Mean":
                    data.append(row[k])
            self.assertEqual(self.statistics.mean(data), float(result))
        print("Mean Test Passed")

    def test_median_statistics(self):
        for row in self.test_data_median:
            result = row["Median"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Median":
                    data.append(row[k])
            self.assertEqual(self.statistics.median(data), float(result))
        print("Median Test Passed")


    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
####UnboundLocalError: local variable 'row' referenced before assignment
        self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
        self.assertEqual(self.statistics.result, float(row['mode']))

###ATypeError: 'module' object is not callable

    # def test_standard_deviation_statistics(self):
    #     for row in self.test_answer:
    #         pprint(row["std"])
    #         ###ATypeError: 'module' object is not callable
    #     self.assertEqual(self.statistics.standardDev(self.column1), float(row['std']))
    #     self.assertEqual(self.statistics.result, float(row['std']))

    # def test_proportion_variance_statistics(self):
    #     for row in self.test_answer:
    #         ##TypeError: 'module' object is not callable
    #         pprint(row['proportion_variance'])
    #     self.assertEqual(self.statistics.proportion(self.column1), float(row['proportion_variance']))
    #     self.assertEqual(self.statistics.result, float(row['proportion_variance']))

    # NameError: name
    # 'zscoreanswers' is not defined
    #
    # def test_correlation_statistics(self):
    #     for row in self.test_answer:
    #         pprint(row['correlation'])
    #     self.assertEqual(self.statistics.correlation_coefficient(self.column1, self.column2),
    #                      float(row['correlation']))
    #     self.assertEqual(self.statistics.result, float(row['correlation']))

    # def test_pvalue_statistics(self):
    #     self.assertEqual(self.statistics.p_value(self.column1), self.column_zscore)
    #     self.assertEqual(self.statistics.result, self.column_zscore)


if __name__ == '__main__':
    unittest.main()