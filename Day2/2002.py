class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"메뉴 : {self.name} / 가격 : {self.price}"

info = input().split()
a = Drinks(info[0], int(info[1]))
print(a)
print(type(a))

