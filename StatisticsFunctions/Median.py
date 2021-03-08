from RandomGenerator.RandomValues import random_numbers
import statistics


def median():
    data_list = random_numbers()

    return statistics.median(data_list)
