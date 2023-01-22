# Домашнє завдання:
# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.'
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

class AddStudentUser(Exception):
    def __init__(self, msg):
        super().__init__()
        self.message = msg
    def __str__(self):
        return str(self.message)

class RemoveStudentUser(Exception):
    def __init__(self, msg):
        super().__init__()
        self.message = msg
    def __str__(self):
        return str(self.message)

class People:

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.surname} {self.name[0]}'


class Student(People):

    def __init__(self,  surname, name, age, descriptions):
        super().__init__(surname, name, age)
        self.descriptions = descriptions

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Group:
    def __init__(self, name, max_students = 10):
        self.name = name
        self.students = []
        self.max_students = max_students

    def __str__(self):
        return '\n'.join(map(str, self.students))

    def add(self, student):
        if len(self.students) >= self.max_students:
            raise AddStudentUser(f" Count users have to be less {self.max_students}")
        else:
            self.students.append(student)

    def remove(self, surname):
        for i in self.students:
            if i.surname == surname:
                self.students.remove(i)
                return "student remove"
        raise RemoveStudentUser("student not remove")

    def search(self, surname):
        for i in self.students:
            if i.surname == surname:
                return i
        return None


gr = Group("KS-00-1")
s = {}
for i in range(15):
    s[i] = Student("surname" + str(i),"name" + str(i), i, "descriptions" + str(i))

for i in range(14):
    try:
        gr.add(s[i])
    except AddStudentUser as er:
        print(er)
        log.exception(er)

print(gr)
try:
    print(gr.remove("surname3"))
except RemoveStudentUser as er:
    print(er)
    log.exception(er)

print(gr)

tmp = gr.search("surname4")

print(tmp.name)

