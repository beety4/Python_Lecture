import operations.add
from operations import minus
from operations.multiply import multiply
from operations.divide import divide as d
#from operations import *

d1 = {'+': operations.add.add, '-': minus.minus, '*': multiply, '/': d.divide}
def calc(operation, num):
    return d1.get(operation)(num)


oper = input("연산자 : ")
num = list(map(int, input("숫자 : ").split()))
print(f"결과 : {calc(oper, num)}")
