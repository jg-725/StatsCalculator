import math


class Operations:
    def __init__(self):
        pass

    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        x = float(x)
        y = float(y)
        answer = y - x
        return answer

    @staticmethod
    def multiplication(x, y):
        return float(x) * float(y)

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError('Unable to divide by zero')
        return float(b) / float(a)

    @staticmethod
    def square(a):
        x = float(a) * float(a)
        return x

    @staticmethod
    def root(a):
        x = float(a)
        return math.sqrt(a)
