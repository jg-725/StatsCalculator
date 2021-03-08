from random import seed
from random import randint
from random import choice


def choose():
    numbers = []
    seed(1)
    pick = 0
    for i in range(10):
        numbers.append(randint(0, 10))

    length = len(numbers)

    for i in range(length):
        pick = choice(numbers)
    return pick
