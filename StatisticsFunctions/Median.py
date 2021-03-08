from RandomGenerator.RandomValues import random_list


def median():
    data = random_list()

    numbers = data
    numbers.sort()

    if data % 2 == 0:
        num1 = numbers[data // 2]
        num2 = numbers[data // 2 - 1]
        final_median = (num1 + num2) / 2
    else:
        final_median = numbers[data // 2]

    return final_median
