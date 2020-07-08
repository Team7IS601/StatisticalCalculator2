import unittest
from Stats.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Statistics = Statistics('/Tests/Data/UnitTestStatsAnswers.csv')

    def test_instantiate_statcalculator(self):
        self.assertIsInstance(self.Statistics, Statistics)