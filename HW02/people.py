from my_except import *


class People:

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name[0]}'
