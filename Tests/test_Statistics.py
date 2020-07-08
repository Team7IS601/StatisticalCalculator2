import unittest
from Stats.Statistics import Statistics
from CsvReader.CsvReader3 import getFileData

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        test_answer = getFileData('Tests/Data/UnitTestStatistics.csv').data
        sample_data = getFileData('Tests/Data/TestSampleData.csv').data

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

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column1), float(row['mode']))
        self.assertEqual(self.statistics.result, float(row['mode']))

if __name__ == '__main__':
    unittest.main()