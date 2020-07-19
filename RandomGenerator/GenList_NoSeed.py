from random import randint
import random


class GenListNoSeed:
    def list_int (x, y, ranges):
        if isinstance(x, float):
            return GenListNoSeed.list_float(x, y, ranges)
        series = []
        for each in range(ranges):
            number = randint(x, y)
            series.append(number)
        return series

    def list_float(x, y, ranges):
        series = []

        for each in range (ranges):
            number = random.uniform(x, y)
            series.append(number)
        return series


print(GenListNoSeed.list_int(4.4,9.7,10))


