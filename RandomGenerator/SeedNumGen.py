from random import seed
from random import randint
import random


def num_seed():
    number = []
    seed(1)
    for i in range(1):
        number.append(randint(0, 10))
    return number


def num_seed_float():
    number = []
    seed(1)
    for i in range(1):
        number.append(random.uniform(.5, 10.5))
    return number
