import random


def random_numbers():
    numbers = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        numbers.append(n)
    return numbers
