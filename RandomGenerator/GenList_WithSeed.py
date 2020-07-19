from random import seed
from random import randint
import random


class GenListWithSeed:
    def list_int (x, y, ranges, nut):
        if isinstance(x, float):
            return GenListWithSeed.list_float(x, y, ranges, nut)
        series = []
        seed(nut)
        for each in range(ranges):
            number = randint(x, y)
            series.append(number)
        return series

    def list_float(x, y, ranges, nut):
        series = []
        seed(nut)
        for each in range (ranges):
            number = random.uniform(x, y)
            series.append(number)
        return series


print(GenListWithSeed.list_float(4,9,10,2))


