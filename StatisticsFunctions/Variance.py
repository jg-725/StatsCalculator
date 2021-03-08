import statistics
from StatisticsFunctions.Mean import mean


def variance():
    mean_value = mean()
    answer = statistics.variance(mean_value)
    return answer
