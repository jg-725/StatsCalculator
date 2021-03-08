from OperationsFile.Operations import Operations
from StatisticsFunctions.Variance import variance


def standard_deviation():
    variance_value = variance()
    answer = Operations.root(variance_value)
    return answer
