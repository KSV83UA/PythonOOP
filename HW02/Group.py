from MyExcept import *

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
            logger.info(f"Student {student} add to group successfully" )

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

