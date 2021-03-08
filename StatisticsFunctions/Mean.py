from OperationsFile import Operations
from RandomGenerator.RandomValues import random_list


def mean():
    random_data = random_list()
    count = len(random_data)
    total = 0

    for num in random_data:
        total = Operations.Operations.addition(total, num)

    return Operations.Operations.division(total, count)
