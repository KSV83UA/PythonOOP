from MyExcept import *


class Customer:
    def __init__(self, name, surname, mobile):
        self._name = name
        self._surname = surname
        self._mobile = mobile

    def set_name(self, name):
        self._name = name
        return True

    def get_name(self):
        return self._name

    def set_surname(self, surname):
        self._surname = surname

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def get_surname(self):
        return self._surname

    def set_mobile(self, mobile):
        self._mobile = mobile

    def get_mobile(self):
        return self._mobile

    def __str__(self):
        return f'{self._name} {self._surname}'

