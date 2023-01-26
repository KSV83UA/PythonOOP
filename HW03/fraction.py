# 2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів
# цього класу.

import math


class ErrorZero(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Fraction():
    def __init__(self, fr1, fr2):
        if fr2 == 0:
            raise ErrorZero("not sub zero")

        self.number1 = fr1
        self.number2 = fr2

    def __str__(self):
        n1 = self.number1
        n2 = self.number2

        if n1 > n2:
            x = n1 // n2
            y = n1 % n2
            if y == 0:
                return f'{int(x)}'
            q = n1 - n2 * x
            g1 = math.gcd(q, n2)
            q //= g1
            n2 //= g1
            return f'{int(x)} {int(q)}/{n2}'

        g = math.gcd(n1, n2)
        n1 //= g
        n2 //= g

        return f"{int(n1)}/{int(n2)}"

    def __eq__(self, other):
        return self.number1 == other.number1 and self.number2 == other.number2

    def _add(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        n1 = self.number1 * other.number2 + other.number1 * self.number2
        n2 = self.number2 * other.number2

        if (n1 % n2):
            x = math.gcd(n1, n2)
            n1 /= x
            n2 /= x

        return Fraction(int(n1), int(n2))

    def __add__(self, other):
        return self._add(self, other)
        # if not isinstance(other, Fraction):
        #     return NotImplemented
        #
        # n1 = self.number1 * other.number2 + other.number1 * self.number2
        # n2 = self.number2 * other.number2
        #
        # if (n1 % n2):
        #     x = math.gcd(n1, n2)
        #     n1 /= x
        #     n2 /= x
        #
        # return Fraction(int(n1), int(n2))

    def __radd__(self, other):
        return self._add(self, other)
        # if not isinstance(other, Fraction):
        #     return NotImplemented
        #
        # n1 = self.number1 * other.number2 + other.number1 * self.number2
        # n2 = self.number2 * other.number2
        #
        # if (n1 % n2):
        #     x = math.gcd(n1, n2)
        #     n1 /= x
        #     n2 /= x
        #
        # return Fraction(int(n1), int(n2))

    def __sub__(self, other):
        n1 = self.number1 * other.number2 - other.number1 * self.number2
        n2 = self.number2 * other.number2

        if n1 % n2:
            x = math.gcd(n1, n2)
            n1 /= x
            n2 /= x

        return Fraction(int(n1), int(n2))

    def __mul__(self, other):
        return Fraction(int(self.number1 * other), int(self.number2))


if __name__ == "__main__":
    fr_1 = Fraction(5, 6)
    fr_2 = Fraction(10, 5)
    fr_3 = Fraction(10, 6)
    print(f'fr_1: {fr_1}')
    print(f'fr_2: {fr_2}')
    print(f'fr_3: {fr_3}')

    print(f'fr_1 == fr_2: {fr_1 == fr_2}')
    print(f'fr_1 + fr_2: {fr_1 + fr_2}')
    print(f'fr_1 + fr_3: {fr_1 + fr_3}')

    print(f'fr_1 + fr_2: {fr_1 - fr_2}')
    print(f'fr_1 + fr_3: {fr_1 - fr_3}')

    fr_4 = fr_1 * 3
    print(f'fr_1 * 3 = {fr_4}')
