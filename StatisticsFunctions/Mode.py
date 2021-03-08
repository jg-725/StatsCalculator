from collections import Counter
from RandomGenerator.RandomValues import random_numbers


def mode():
    num_data = random_numbers()
    count = Counter(num_data)
    mode_total = dict(count)
    answer = [k for k, v in mode_total.items() if v == max(list(count.values()))]
    return answer
