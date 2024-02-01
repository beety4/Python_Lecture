class Tclass:
    a = 0
    b = 0

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def test(self):
        print(self.a)

    def edit(self, a):
        self.a = a


# ins = Tclass()
# ins.edit(9)
# ins.test()
#
# other = Tclass()
# other.test()
#
# print(ins is other)


cs = Tclass(3, 4)
cs.test()

other = Tclass()
other.a = 3
other.b = 4
