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
        #Считаем, что не передаем сюда целые числа, иначе 0 в переменной fr2 обозначал бы передачу целого числа
        #в данном случае делаем исключение, так как класс про дроби, а они на 0 не делятся )

        if fr2 == 0:
            raise ErrorZero("not sub zero")

        self.int_number = 0
        self.number1 = fr1
        self.number2 = fr2

    def __str__(self):
        x = 1
        if self.int_number == 0:
            return f'{self.number1}/{self.number2}'
        return f"{self.int_number} {self.number1}/{self.number2}"

    def __eq__(self, other):
        return self.number1 == other.number1 and self.number2 == other.number2



if __name__ == "__main__":
    fr_1 = Fraction(5,6)
    fr_2 = Fraction(10,5)
    print(f'fr_1: {fr_1}')
    print(f'fr_2: {fr_2}')


    print(f'fr_1 == fr_2: {fr_1 == fr_2}')

