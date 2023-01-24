# Домашнє завдання:
# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.'
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

from MyExcept import *

import People
import Student
import Group

gr = Group.Group("KS-00-1")
s = {}
for i in range(15):
    s[i] = Student.Student("surname" + str(i),"name" + str(i), i, "descriptions" + str(i))

for i in range(14):
    try:
        gr.add(s[i])
    except AddStudentUser as er:
        print(er)
        logger.exception(er)

print(gr)
try:
    print(gr.remove("3"))
except RemoveStudentUser as err:
    print(err)
    logger.exception(err)

print(gr)

tmp = gr.search("surname4")

print(tmp.name)

