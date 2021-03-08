from OperationsFile.Operations import Operations
from StatisticsFunctions.Mean import mean
from StatisticsFunctions.Stand_Dev import standard_deviation


def z_score():
    x_value = float(mean())
    y_value = float(standard_deviation())

    sub = Operations.subtraction(x_value, 5)
    result = Operations.division(y_value, sub)
    return result
