from OperationsFile.Operations import Operations
from StatisticsFunctions.Variance import variance


def standard_deviation():
    variance_value = variance()
    return Operations.root(variance_value)
