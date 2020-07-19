from RandomGenerator.GenList_WithSeed import GenListWithSeed
from RandomGenerator.GenList_NoSeed import GenListNoSeed
from RandomGenerator.GenNum_NoSeed import GenNumNoSeed
from RandomGenerator.GenNum_WithSeed import GenNumWithSeed

print()

if __name__ == '__main__':
    print(GenListWithSeed.list_int(1, 10, 5, 4), "Tested List With Seed")
    print(GenListNoSeed.list_int(1, 10, 5), "Tested List With NO Seed")
    print(GenNumNoSeed.num_int(1, 10), "Tested Number NO Seed - Interger")
    print(GenNumNoSeed.num_int(1.4, 10.4), "Tested Number NO Seed -- Float")
    print(GenNumWithSeed.num_int(1, 10, 5), "Tested Number With Seed - Interger")
    print(GenNumWithSeed.num_int(1.1, 10.4, 5), "Tested Number With Seed - Float")
