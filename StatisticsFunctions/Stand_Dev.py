from OperationsFile.Operations import Operations
from StatisticsFunctions.Variance import variance
import math


def standard_deviation():
    variance_value = variance()

    # answer = Operations.root(variance_value)

    answer = math.sqrt(variance_value)

    return answer
