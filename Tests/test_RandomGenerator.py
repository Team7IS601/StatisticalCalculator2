from RandomGenerator.random import random
from pprint import pprint
from Stats.RandomGenerators import list_generator
import Stats.RandomGenerators

def test_something(self):
    # List evaluates to False if empty
    test_list = Stats.RandomGenerators.list_generator()
    self.assertTrue(test_list)


def test_random_item(self):
    # test default list count
    test_list = Stats.RandomGenerators.list_generator()
    self.assertEqual(len(test_list), 100)


def test_random_seed(self):
    seed_val = 6
    choice = Stats.RandomGenerators.random_seed(seed=seed_val)
    self.result = seed_val
    self.assertEqual(self.result, 6)