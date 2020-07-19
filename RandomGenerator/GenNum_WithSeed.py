from random import randint
import random


class GenNumWithSeed:
    def num_int (x, y, nut):
        if isinstance(x, float):
            return GenNumWithSeed.num_float(x, y, nut)
        random.seed(nut)
        return randint(x, y)

    def num_float(x, y, nut):
        random.seed(nut)
        return random.uniform(x, y)

print(GenNumWithSeed.num_int(3,8,10))