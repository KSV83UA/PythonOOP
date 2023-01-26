# Домашнє завдання:
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису
# товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон
# тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
# про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
# для коректного виведення інформації про це замовлення.

from my_except import *
import product
import customer
import order


try:
    product1 = product.Product('apple', 12.00, 1, 'green apple')
    product2 = product.Product('orange', 14.00, 1, 'orange Egypt')
    product3 = product.Product('carrot', 1.00, 1, 'carrot Ukraine')
    product4 = product.Product('raspberry', -122.00, 1, 'raspberry fresh')
except ErrorPrice as er:
    print(er)

cust = customer.Customer('name', 'surname', '123123123')

order1 = order.Order(cust)
try:
    order1.add_product(product1, 8)
    order1.add_product(product2, 5)
    order1.add_product(product3, -1)
    order1.add_product(product4, 6)
except ErrorCounts as er:
    print(er)
print(str(order1))
