# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
#  Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на
#  завершення.
# 2. Реалізуйте свій аналог генераторної функції range().
# 3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром
# цієї функції.
# 4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної
# вами величини.

def gen_1(step, max=10,flag=0, stop=None):
    for i in range(1, max):
        stop = yield i * step
        if stop == flag:
            return None


x = gen_1(3)

for i in x:
    print(f'item number: {i / 3 + 1:.0f} - number {i}')
    if i > 10:
        try:
            x.send(0)
        except StopIteration as e:
            pass


def my_range(*args):
    i = 0
    if len(args) == 1:
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3:
        i = args[0]
        while i < args[1]:
            yield i
            i += args[2]
    else:
        raise TypeError


for i in my_range(1,10,2):
    print(i)


def count(max_number):
    if not isinstance(max_number, int):
        raise TypeError
    for it in range(2, max_number):
        flag = True
        for j in range(2, it):
            if it % j == 0:
                flag = False
                break
        if flag:
            yield it

c = count(20)

for i in c:
    print(f'number right: {i}')


def get_cube(number):
    for i in range(2, number):
        yield i * 3


l = [i for i in get_cube(20)]
print(l)


