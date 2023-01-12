# Домашнє завдання:
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису
# товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон
# тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
# про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
# для коректного виведення інформації про це замовлення.
class Product:
    def __init__(self, name, price, weight, description):
        self._weight = weight
        self._name = name
        self._price = price
        self._description = description,

    def set_price(self, price):
        self._price = price
        return True

    def set_weight(self, weight):
        self._weight = weight
        return True

    def set_name(self, name):
        self._name = name
        return True

    def set_description(self, description):
        self._description = description
        return True

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
        return True

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def get_surname(self):
        return self._surname

    def set_mobile(self, mobile):
        self._mobile = mobile
        return True

    def get_mobile(self):
        return self._mobile

    def __str__(self):
        return f'{self._name} {self._surname}'


class Order:
    def __init__(self, customer):
        self._customer = customer
        self._product = []

    def add_product(self, product, count):
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



product1 = Product('apple', 12.00, 1, 'green apple')
product2 = Product('orange', 14.00, 1, 'orange Egypt')
product3 = Product('carrot', 1.00, 1, 'carrot Ukraine')
product4 = Product('raspberry', 122.00, 1, 'raspberry fresh')

cust = Customer('Serhii', 'Kushnirenko', '+380979224994')

order1 = Order(cust)

order1.add_product(product1, 8)
order1.add_product(product2, 5)
order1.add_product(product3, 1)
order1.add_product(product4, 6)

print(str(order1))
