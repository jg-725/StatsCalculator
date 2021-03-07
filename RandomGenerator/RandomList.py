from random import seed
from random import randint


def random_list():
    numbers = []
    seed(2)
    for i in range(10):
        numbers.append(randint(0, 10))
    return numbers
