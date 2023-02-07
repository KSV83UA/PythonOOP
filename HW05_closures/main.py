# Домашнє завдання:
# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається
# за допомогою функції користувача.
#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
#  що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого
# списку.

import timeit
from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

def fun1(start, stop, user_fun):
    while start < stop:
        start = user_fun(start)
        tmp = yield start
        if tmp:
            return

x = fun1(1, 10, lambda x: x * 2)

for i in x:
    print(i)


# **********************************************************#


def fun2():
    x = [0,1, 1]

    def mem_fun(n):
        if len(x) >= n:
            return x[n]
        for i in range(len(x), n + 1):
            res = int(x[-2]) + int(x[-1])
            # res += x
            x.append(res)
        return res

    return mem_fun

def fun3(n):
    if n == 1 or n ==2:
        return 1
    return  fun3(n-1) + fun3(n-2)


@lru_cache()
def fun4(n):
    if n == 1 or n ==2:
        return 1
    return  fun3(n-1) + fun3(n-2)


tmp1, element, element2 = fun2(), 6, 5


print(f'Фибоначи рекурсия первый запуск, число({element}): {timeit.timeit(stmt="fun3(element)", setup="from __main__ import fun3, element")}')
print(f'Фибоначи рекурсия с кешем первый запуск, число({element}): {timeit.timeit(stmt="fun4(element)", setup="from __main__ import fun4, element")}')
print(f'Фибоначи замыкание с кешем первый запуск, число({element}): {timeit.timeit(stmt="tmp1(element)", setup="from __main__ import tmp1, element")}')
print("\n")
print(f'Фибоначи рекурсия второй запуск, число({element}): {timeit.timeit(stmt="fun3(element2)", setup="from __main__ import fun3, element2")}')
print(f'Фибоначи рекурсия с кешем второй запуск, число({element}): {timeit.timeit(stmt="fun4(element2)", setup="from __main__ import fun4, element2")}')
print(f'Фибоначи замыкание с кешем второй запуск, число({element}): {timeit.timeit(stmt="tmp1(element2)", setup="from __main__ import tmp1, element2")}')


def fun5(my_list, fun):
    return sum((fun(i) for i in my_list))

print(fun5([1,2,3], lambda x : x*2))

