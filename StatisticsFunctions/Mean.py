from OperationsFile import Operations
from RandomGenerator.RandomValues import random_numbers


def mean():
    sample_values = random_numbers()
    total = 0
    count = len(sample_values)

    for num in sample_values:
        total = Operations.Operations.addition(total, num)

    return Operations.Operations.division(total, float(count))
