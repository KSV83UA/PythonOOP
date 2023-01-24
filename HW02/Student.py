from MyExcept import *

import People

class Student(People.People):

    def __init__(self,  surname, name, age, descriptions):
        super().__init__(surname, name, age)
        self.descriptions = descriptions

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'

