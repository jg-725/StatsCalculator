import unittest
from src.Calculator import Calculator
from OperationsFile.Operations import Operations


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        answer = Operations.addition(5, 4)
        self.assertEqual(answer, 9)

    def test_subtraction(self):
        answer = Operations.subtraction(4, 6)
        self.assertEqual(answer, 2)

    def test_multiply(self):
        answer = Operations.multiplication(4, 6)
        self.assertEqual(answer, 24)

    def test_division(self):
        answer = Operations.division(4, 8)
        self.assertEqual(answer, 2)

    def test_square_root(self):
        answer = Operations.root(4)
        self.assertEqual(answer, 2)

    def test_square(self):
        answer = Operations.square(4)
        self.assertEqual(answer, 16)


if __name__ == '__main__':
    unittest.main()
