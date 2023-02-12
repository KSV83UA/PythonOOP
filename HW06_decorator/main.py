# Домашнє завдання:
# 1. Створіть декоратор, який підраховуватиме, скільки разів була викликана декорована функція.
# 2. Створіть декоратор, який зареєструє декоровану функцію у списку.
# 3. Припустимо, у класі визначено метод str. Створіть такий декоратор для цього методу,
# щоб отриманий рядок зберігався у текстовий файл. Ім'я файлу має збігатися з ім'ям класу, в якому визначено метод str.
# 4. Створіть декоратор із параметрами для проведення хронометражу роботи тієї чи іншої функції. Параметрами повинні
# виступати те, скільки разів потрібно запустити функцію, що декорується, і в який файл зберегти результати хронометражу.

import time

######    1    ##########
def decorator_counter(func):
    decorator_counter.count = 0
    def inner(*args, **kwargs):
        decorator_counter.count += 1
        return f'{func(*args, **kwargs)} + decor'
    return inner

@decorator_counter
def f_counter(name):
    return f'name: {name}'

for _ in range(4):
    f_counter('asd')

print(f'count interation: {decorator_counter.count}')

######    2    ##########
list_fun = []

def decor_list(fun):
    list_fun.append(fun)
    return fun
@decor_list
def fun_mul(x, y):
    return x * y
@decor_list
def fun_add(x, y):
    return x + y

fun_mul(2,3)
fun_add(4,5)
print(list_fun)

######    3    ##########

def decor_str(fun):
    def c_str(*args, **kwargs):
        text = fun(*args, **kwargs)
        file_name = type(args[0]).__name__
        with open(file_name, 'a+') as f:
            f.write(text)
        return text
    return c_str

class My_1:
    def __init__(self):
        self.line = "this line in class"

    @decor_str
    def __str__(self):
        return self.line


x = My_1()
print(x)

##### 4 #######

class DecorTime:
    def __init__(self, count, file_name):
        self.count = count
        self.file_name = file_name
        self.start = None
        self.stop = None

    def __call__(self, fun, *args, **kwargs):
        def inner(*args, **kwargs):
            with open(self.file_name, 'a+') as f:
                self.start = time.time()
                f.write(f'start {fun.__name__} : {self.start} ')
                for _ in range(self.count):
                    result = fun(*args, **kwargs)
                self.end = time.time()
                f.write(f' end {fun.__name__} : {self.end}\n')
            return result
        return inner

@DecorTime(5, "test.txt")
def fibo(n):
    if n == 1 or n ==2:
        return 1
    return  fibo(n-1) + fibo(n-2)

print(fibo(5))



