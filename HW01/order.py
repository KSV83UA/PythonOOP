from my_except import *


class Order:
    def __init__(self, customer):
        self._customer = customer
        self._product = []

    def add_product(self, product: object, count: object) -> object:
        if count <= 0:
            raise ErrorCounts("Count have to  be more 0")
        self._product.append({"product": product, "count": count})

    def get_all_product(self):
        all_product = ""
        for i in self._product:
            all_product += f'name:{i["product"].get_name()} \\ count: {i["count"]} \\ price: {i["product"].get_price():.2f}$  \\ Summa: {i["product"].get_price() * i["count"]} \n'
        return all_product

    def get_summ(self):
         summ = 0
         for i in self._product:
             summ += i["product"].get_price() * i["count"]
         return summ

    def remove_product(self, product):
        pass

    def __str__(self):
        return f'Customer: {self._customer.get_full_name()} \nProduct:\n{self.get_all_product()}\nOrder summa: {self.get_summ():.2f}$'
