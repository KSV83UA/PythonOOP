# 1. Створіть декоратор, який зареєструє декорований клас у списку.
#test
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
class DecorOrder:
    def __init__(self, cls):

        self.cls = cls
class Order:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError

        self.number = number

    def __str__(self):
        return str(self.number)

# 3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.

# 4. Створіть дескриптор, який робитиме поля доступними лише для читання.
# 5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел.
# 6. Реалізуйте властивість класу, яка має наступний функціонал: при установці значення цієї властивості у файл із
# заздалегідь визначеним ім'ям повинен зберігатися час (коли встановлювали значення властивості) та встановлене значення.
# 7. Створіть ABC клас із абстрактним методом перевірки цілого числа на простоту. Тобто якщо параметром цього методу є
# ціле число і воно просте, то метод повинен повернути True, а в іншому випадку False. Створіть похідний клас. Перевірте
# працездатність проекту.