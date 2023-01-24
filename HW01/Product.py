from MyExcept import *


class Product:

    def __init__(self, name, price, weight, description):
        if price <= 0:
            raise ErrorPrice("Price have to be more 0")
        self._weight = weight
        self._name = name
        self._price = price
        self._description = description

    def set_price(self, price):
        if price <= 0:
            raise ErrorPrice("Price have to be more 0")
        self._price = price

    def set_weight(self, weight):
        self._weight = weight

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def get_price(self):
        return self._price

    def get_weight(self):
        return self._weight

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def __str__(self):
        return self._name


