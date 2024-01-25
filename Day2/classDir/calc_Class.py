class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def minus(self, a, b):
        self.result = a - b

    def multiply(self, a, b):
        self.result = a * b

    def divide(self, a, b):
        self.result = a / b

    def getResult(self):
        return self.result


c1 = Calculator()
c1.add(4, 5)
print(c1.getResult())

c1.minus(5, 1)
print(c1.getResult())

c2 = Calculator()
print(c2.getResult())
