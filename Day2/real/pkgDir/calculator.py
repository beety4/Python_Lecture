import operations.add
from operations import minus
from operations.divide import divide
from operations import multiply as m

# lst = [3, 2]
# result = operations.add.add(lst)
# print(result)
#
# result2 = minus.minus(lst)
# print(result2)
#
# result3 = divide(lst)
# print(result3)
#
# result4 = m.multiply(lst)
# print(result4)

d1 = {
    '+': operations.add.add,
    '-': minus.minus,
    '*': m.multiply,
    '/': divide
}

def calc(operation, nums):
    return d1.get(operation)(nums)


# + - * /
oper = input("연산자 : ")
# 3 4 5  -> [3, 4, 5]
nums = list(map(int, input("숫자 : ").split()))
print(f"결과 : {calc(oper, nums)}")
