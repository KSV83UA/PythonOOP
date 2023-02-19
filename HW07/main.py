# 1. Створіть декоратор, який зареєструє декорований клас у списку.
from time import time

class_list = []

class ListAdd:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        result = self.cls(*args, **kwargs)
        class_list.append(result)
        return result


@ListAdd
class Student:
    def __init__(self ,name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

x = Student('Alex', 'Pupkin')
y = Student('Alex', 'Pupkin2')

print(x)
print(y)
print(class_list)

# 2. Створіть клас декоратора з параметром. Параметром має бути рядок, який повинен дописуватись (ліворуч) до результату
# роботи методу str.
def DecorOrder(fun):
    line = "Secret: "
    def inner(*args, **kwargs):
        return f'{line} {fun(*args, **kwargs)}'
    return inner


class Order:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError

        self.number = number

    @DecorOrder
    def __str__(self):
        return str(self.number)

x = Order(10)
print(x)

# 3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.

class Box:
    def __init__(self, x, y, z):
        if not isinstance(x, int|float) or not isinstance(y, int | float) or not isinstance(z, int | float):
            raise TypeError
        self.x = x
        self.y = y
        self.z = z

    def v(self):
        return self.x * self.y * self.y

    def __str__(self):
        return f'{x} x {y} x {z}'

    @staticmethod
    def sum_v(box1, box2):
        return box1.v() + box2.v()

box_1 = Box(4,2,4)
box_2 = Box(5,6,3)
print("v = " + str(Box.sum_v(box_1, box_2)))
print(x)

# 4. Створіть дескриптор, який робитиме поля доступними лише для читання.
class OrderDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = value
        pass

    def __delete__(self, instance):
        pass


class Cart:
    def __init__(self, title, order):
        self.title = title
        self.order = order

    order = OrderDescriptor('order')

    def __str__(self):
        return str(self.order)



x_1 = Cart('order', 10)
x_1.order = 20
print(f'desc: {x_1}')

# 5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел.
class Number:

    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError
        self.__dict__[key] = value

    def __str__(self):
        return str(self.value)

x_2 = Number(10)
print(x_2)
x_2.value = 12
# x_2.value = "asdasd"
print("integer=", (x_2))

# 6. Реалізуйте властивість класу, яка має наступний функціонал: при установці значення цієї властивості у файл із
# заздалегідь визначеним ім'ям повинен зберігатися час (коли встановлювали значення властивості) та встановлене значення.
class Cls1:
    def __init__(self, value):
        self.file_name = "cls1.txt"
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        with open(self.file_name, "a") as fls:
            fls.write(f'{time()} : value={value}\n')
        self.__value = value

    def __str__(self):
        return str(self.value)

    @value.deleter
    def value(self):
        pass


x_3 = Cls1(10)
x_3.value = 20
print(f'x_3: {x_3}')

# 7. Створіть ABC клас із абстрактним методом перевірки цілого числа на простоту. Тобто якщо параметром цього методу є
# ціле число і воно просте, то метод повинен повернути True, а в іншому випадку False. Створіть похідний клас. Перевірте
# працездатність проекту.

from abc import ABC, abstractmethod

class IsSimple(ABC):
    @abstractmethod
    def is_simple(self, number):
        pass

class CheckNumber(IsSimple):
    def __init__(self):
        pass

    def is_simple(self, number):
        if not isinstance(number, int):
            return False
        for i in range(2, (number // 2) + 1):
            if not number % i:
                return False
        return True


x_4 = CheckNumber()
print(x_4.is_simple(11))
