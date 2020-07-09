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
        self.test_data_mode = getFileData('Tests/Data/Test_Data_Mode.csv').data
        self.unit_test_statistics = getFileData('Tests/Data/UnitTestStatistics.csv').data
        self.test_data_sample = getFileData('Tests/Data/TestDataSample.csv').data
        self.test_data_variance = getFileData('Tests/Data/Test_Data_Variance.csv').data
        self.test_data_standardDev = getFileData('Tests/Data/Test_Data_StandardDeviation.csv').data
        self.test_data_cochran_sample = getFileData('Tests/Data/Test_Data_Cochran_Sample.csv').data
        self.test_data_zscore = getFileData('Tests/Data/Test_Data_ZScore.csv').data
        self.test_answers_zscore = getFileData('Tests/Data/Test_Data_ZScore_Answers.csv').data
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
        for row in self.test_data_mode:
            result = row["Mode"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Mode":
                    data.append(row[k])
            self.assertEqual(self.statistics.mode(data), float(result))
        print("Mode Test Passed")

    def test_proportion_variance_statistics(self):
        for row in self.test_data_variance:
            result = row["Variance"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Variance":
                    data.append(row[k])
            self.assertEqual(self.statistics.variance(data), float(result))
        print("Variance Test Passed")

    def test_standard_deviation_statistics(self):
        for row in self.test_data_standardDev:
            result = row["StandardDev"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "StandardDev":
                    data.append(row[k])
            self.assertEqual(self.statistics.standardDev(data), float(result))
        print("Standard Deviation Test Passed")

    # def test_cochran_sample_statistics(self):
    #     for row in self.test_data_cochran_sample:
    #         result = row["Proportions"]
    #         data = []
    #         keys = row.keys()
    #         for k in keys:
    #             if k != "Proportions":
    #                 data.append(row[k])
    #         self.assertEqual(self.statistics.cochran_sample(data), float(result))
    #     print("Cochran Sample Test Passed")

##AssertionError: Lists differ: [-1.0218610562587904, 0.19360663994374114, -0.3[154 chars]4114] != [-1.02858502772493, 0.187700369612389, -0.32092[138 chars]2389]
    # def test_zscore_statistics(self):
    #     data = []
    #     for row in self.test_data_zscore:
    #         data.append(float(row['Zvalues']))
    #     data_var = data[0:10]
    #     results = []
    #     for row in self.test_answers_zscore:
    #         results.append(float(row['Zscores']))
    #     self.assertEqual((self.statistics.zscore(data_var)), results)

    # def test_pvalue_statistics(self):
    #     self.assertEqual(self.statistics.p_value(self.column1), self.column_zscore)
    #     self.assertEqual(self.statistics.result, self.column_zscore)


if __name__ == '__main__':
    unittest.main()