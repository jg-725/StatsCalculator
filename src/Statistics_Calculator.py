from src.Calculator import Calculator
from StatisticsFunctions.Mean import mean
from StatisticsFunctions.Mode import mode
from StatisticsFunctions.Median import median
from StatisticsFunctions.Stand_Dev import standard_deviation
from StatisticsFunctions.Variance import variance
from StatisticsFunctions.Z_Score import z_score


class Statistics(Calculator):

    def mean_value(self):

        self.result = mean()
        return self.result

    def median_value(self):
        self.result = median()
        return self.result

    def mode_value(self):
        self.result = mode()
        return self.result

    def standard_value(self):
        self.result = standard_deviation()
        return self.result

    def variance_value(self):
        self.result = variance()
        return self.result

    def z_score_value(self):
        self.result = z_score()
        return self.result

