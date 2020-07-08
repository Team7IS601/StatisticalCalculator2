import unittest
import pprint
from Stats.Statistics import Statistics
from CsvReader.CsvReader3 import getFileData


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
    test_answer = getFileData('Tests/Data/UnitTestStatisticsAnswers.csv').data
    test_data = getFileData('Tests/Data/TestData.csv').data
    sample_data = getFileData('Tests/Data/TestDataSample.csv').data
    column1 = [int(row['Value 1']) for row in test_data]
    column2 = [int(row['Value 2']) for row in test_data]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = getFileData('Tests/Data/UnitTestStatistics.csv').data
        for row in test_data:
            result = 'mean'
            self.assertEqual(self.statistics.mean(self.data, result))

    # def test_median_statistics(self):
    #     test_data = getFileData('Tests/Data/UnitTestStatistics.csv')
    #     for row in test_data:
    #         pprint(row["median"])
    #         self.assertEqual(self.statistics.median(self.column1), float(row['median']))
    #         self.assertEqual(self.statistics.result, float(row['median']))


#     def test_mode_statistics(self):
#         for row in self.test_answer:
#             pprint(row["mode"])
# ####UnboundLocalError: local variable 'row' referenced before assignment
#         self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
#         self.assertEqual(self.statistics.result, float(row['mode']))

###AttributeError: 'MyTestCase' object has no attribute 'pprint'

    # def test_standard_deviation_statistics(self):
    #     for row in self.test_answer:
    #         pprint(row["std"])
    #     self.assertEqual(self.statistics.standardDev(self.column1), float(row['std']))
    #     self.assertEqual(self.statistics.result, float(row['std']))

    def test_proportion_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['proportion_variance'])
        self.assertEqual(self.statistics.proportion(self.column1), float(row['proportion_variance']))
        self.assertEqual(self.statistics.result, float(row['proportion_variance']))


if __name__ == '__main__':
    unittest.main()