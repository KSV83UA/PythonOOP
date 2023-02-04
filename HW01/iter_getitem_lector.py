class CartIterator:
    def __init__(self, products, quantities):
        self.products = products
        self.quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration

class Product:

    def __init__(self, title, price, currency='UAH'):
        self.title = title
        self.price = price
        self.currency = currency

    def __str__(self):
        return f'{self.title}: {self.price} {self.currency}'

class Cart:

    def __init__(self, *args, **kwargs):

        self.__products = []
        self.__quantities = []

        if args:
            for item in args:
                if len(item) == 2 and isinstance(item[0], Product) and isinstance(item[1], int | float):
                    self.__products.append(item[0])
                    self.__quantities.append(item[1])


    def add_product(self, product, quantity=1):
        self.__products.append(product)
        self.__quantities.append(quantity)

    def __iter__(self):
        return CartIterator(self.__products, self.__quantities)

    def __getitem__(self, item):
        if isinstance(item, int):
            product = self.__products[item]
            quantity = self.__quantities[item]
            return product, quantity
        if isinstance(item, slice):
            products = self.__products[item]
            quantities = self.__quantities[item]
            return Cart([(product, quantity) for product, quantity in zip(products, quantities)])
        raise TypeError()

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        res = ''
        for product, quantity in self:
            res += f'{product.title} x {quantity} = {product.price * quantity} {product.currency}\n'
        return res



x_1 = Product('apple', 25)
x_2 = Product('banana', 35)
x_3 = Product('orange', 45)
x_4 = Product('lemon', 55)
order = Cart()
order.add_product(x_1, 1.5)
order.add_product(x_2, 3)
order.add_product(x_3, 2.5)
order.add_product(x_4, 0.5)

#print(order)


res = order[1:-1]
print(len(res))

#for product, quantity in order:
    # print(product, quantity)