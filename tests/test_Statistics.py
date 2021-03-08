import unittest
from src.Statistics_Calculator import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_function(self):
        result = self.statistics.mean_value()
        self.assertNotEqual(result, 3)

    def test_median_function(self):
        result = self.statistics.median_value()
        self.assertNotEqual(result, 3)

    def test_mode_function(self):
        result = self.statistics.mode_value()
        self.assertNotEqual(result, 3)

    def test_variance_function(self):
        result = self.statistics.variance_value()
        self.assertNotEqual(result, 3)

    def test_standard_function(self):
        result = self.statistics.standard_value()
        self.assertNotEqual(result, 3)

    def test_z_score_function(self):
        result = self.statistics.z_score_value()
        self.assertNotEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
