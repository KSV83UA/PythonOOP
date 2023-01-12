class Test:
    def __init__(self):
        self._prod = []
    def add(self, p):
        self._prod.append(p)

x = [1,2,3,4]
print(f'number: {map(str,x).__str__()}')