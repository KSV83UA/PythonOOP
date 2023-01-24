# Домашнє завдання:
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису
# товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон
# тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
# про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
# для коректного виведення інформації про це замовлення.

from MyExcept import *
import Product
import Customer
import Order


try:
    product1 = Product.Product('apple', 12.00, 1, 'green apple')
    product2 = Product.Product('orange', 14.00, 1, 'orange Egypt')
    product3 = Product.Product('carrot', 1.00, 1, 'carrot Ukraine')
    product4 = Product.Product('raspberry', -122.00, 1, 'raspberry fresh')
except ErrorPrice as er:
    print(er)

cust = Customer.Customer('name', 'surname', '123123123')

order1 = Order.Order(cust)
try:
    order1.add_product(product1, 8)
    order1.add_product(product2, 5)
    order1.add_product(product3, -1)
    order1.add_product(product4, 6)
except ErrorCounts as er:
    print(er)
print(str(order1))
