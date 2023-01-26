# Домашнє завдання:
# 1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння прямокутників за площею.
# Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників,
# які ви складаєте).
# Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).

class ErrorRec(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class Rectangle():

    def __init__(self, weight, height):
        if weight <= 0 or height <= 0:
            raise ErrorRec("Rectangle will be more zero")

        self.weight = weight
        self.height = height

    def __str__(self):
        return f"{self.weight}x{self.height}"

    def area(self):
        return self.weight * self.height

    def __add__(self, other):
        # так как по идее должны вернуть истанс  то пойдем путем суммирования площадей прямоугольников и делим их на
        # 2 для получения нового прямоугольника

        return Rectangle((self.area() + other.area())/2, 2)

        #  return Rectangle(self.weight + other.weight, self.height + other.height)
        #  если нужно сложить стороны
        # OR
        # return self.area() + other.area()
        # если хотим чтобы работало не правильно

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __mul__(self, other):
        self.weight *= other
        self.height *= other
        return self

if __name__ == "__main__":

    try:
        rec_1 = Rectangle(2,2)
        rec_2 = Rectangle(3,3)
        rec = Rectangle(0,0)
    except ErrorRec as er:
        print(er.msg)

    print(f'{rec_1} area1: {rec_1.area()}')
    print(f'{rec_2} area2: {rec_2.area()}')

    print(f"area1 < area2: {rec_1 < rec_2}")
    print(f"area1 > area2: {rec_1 > rec_2}")
    print(f"area1 == area2: {rec_1 == rec_2}")
    print(f"area1 != area2: {rec_1 != rec_2}")
    print(f"area1 >= area2: {rec_1 >= rec_2}")
    print(f"area1 <= area2: {rec_1 <= rec_2}")


    try:
     rec_3 = rec_1 + rec_2
    except ErrorRec as er:
        print(er.msg)


    print(f'{rec_3} area: {rec_3.area()}')

    print(f'rec_1 + rec_3 + rec_3 = {(rec_3 + rec_2 + rec_1).area()}')
    print(f'rec_3: {rec_3} area {rec_3.area()}')
    rec_3 *= 3
    print(f'"rec_3 *= 3" : {rec_3} area {rec_3.area()}')