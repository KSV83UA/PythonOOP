from my_except import *
import product

class OrderIter:
    def __init__(self, wrapper):
        self.index = 0
        self.wrapper = wrapper

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wrapper):
            raise StopIteration
        self.index += 1
        return self.wrapper[self.index - 1]


class Order:
    def __init__(self, customer):
        self._customer = customer
        self._product = []
        self.count = []

    def __iter__(self):
        return OrderIter(self._product)

    def __getitem__(self, index):
        if isinstance(index, slice):
            result = []
            start = 0 if index.start == None else index.start
            stop = len(self._product) - 1 if index.stop == None else index.stop
            step = 1 if index.step == None else index.step
            for i in range(start, stop, step):
                result.append(self._product[i])
            return result
        if isinstance(index, int):
            if index < 0 or index >= len(self._product):
                raise IndexError
            return self._product[index]

        return TypeError
    def __len__(self):
        return len(self._product)

    def add_product(self, product, count):
        if count <= 0:
            raise ErrorCounts("Count have to  be more 0")
        if product in self._product:
            raise None
        self._product.append(product)
        self.count.append(count)

    def get_all_product(self):
        all_product = ""
        for i,j in zip(self._product, self.count):
            all_product += f'name:{i.get_name()} \\ count: {j} \\ price: {i.get_price():.2f}$  \\ Summa: {i.get_price() * j} \n'
        return all_product

    def get_summ(self):
         summ = 0
         for i,j in zip(self._product, self.count):
             summ += i.get_price() * j
         return summ

    def remove_product(self, product):
        pass

    def __str__(self):
        return f'Customer: {self._customer.get_full_name()} \nProduct:\n{self.get_all_product()}\nOrder summa: {self.get_summ():.2f}$'
