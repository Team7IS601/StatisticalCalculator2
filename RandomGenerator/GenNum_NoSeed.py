from random import randint
import random


class GenNumNoSeed:
    ##Generates Random Numbers without Decimals are used in test.
    def num_int (x, y):
        if isinstance(x, float):
            return GenNumNoSeed.num_float(x, y)
        return randint(x, y)

    ##Defaults to FLOAT when decimals are used in test.
    def num_float(x, y):
        return random.uniform(x, y)

print(GenNumNoSeed.num_int(3,8))