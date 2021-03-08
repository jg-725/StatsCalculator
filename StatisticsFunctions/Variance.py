import statistics
from StatisticsFunctions.Mean import mean


def variance():
    mean_value = mean()
    for i in range(1, int(mean_value) + 1):
        answer = statistics.variance(mean_value)
        return answer
