def fun_1():
    prev, current = 0 ,1

    def get_next():
        nonlocal prev, current
        x1 = prev + current
        prev = current
        current = x1
        return x1
    return get_next

x_1 = fun_1()

while True:
    tmp = x_1()
    print(tmp)
    if tmp > 100:
        break