import unittest

from src.CSVreader import CsvReader
from src.Calculator import Calculator
from OperationsFile.Operations import Operations


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_calc(self):
        unit_data = CsvReader('./tests/unitTests/UnitTestAddition').data
        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), answer)
            self.assertEqual(self.calculator.result, answer)

    def test_sub_calc(self):
        unit_data = CsvReader('/tests/unitTests/UnitTestSubtraction').data

        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), answer)
            self.assertEqual(self.calculator.result, answer)

    def test_multiply_calc(self):
        unit_data = CsvReader('/tests/unitTests/UnitTestMultiplication').data

        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), answer)
            self.assertEqual(self.calculator.result, answer)

    def test_divide_calc(self):
        unit_data = CsvReader('/tests/unitTests/UnitTestDivision').data

        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), answer)
            self.assertEqual(self.calculator.result, answer)
            self.assertRaises(ZeroDivisionError, Operations, 1, 0)

    def test_root_calculator(self):
        unit_data = CsvReader('tests/unitTests/UnitTestSquareRoot').data

        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1']), answer)
            self.assertEqual(self.calculator.result, answer)

    def test_square_calculator(self):
        unit_data = CsvReader('tests/unitTests/UnitTestSquare').data

        for row in unit_data:
            answer = float(row['Result: '])
            self.assertEqual(self.calculator.add(row['Value 1']), answer)
            self.assertEqual(self.calculator.result, answer)


if __name__ == '__main__':
    unittest.main()
