

class Calculator:

    def __init__(self, name):
        self.name = 'Casio'

    def add(self, x, y):
        print(f'{x} + {y} = {x+y}')

    def sub(self, x, y):
        print(f'{x} - {y} = {x-y}')

    def mul(self, x, y):
        print(f'{x} * {y} = {x*y}')

    def div(self, x, y):
        print(f'{x} / {y} = {x/y:.3}')

if __name__ == "__main__":

    c = Calculator('Casio')
    c.add(2,3)
    c.sub(2,3)
    c.mul(2,3)
    c.div(2,3)
