import os

f = open("test.txt", 'r')
n = f.readline()
f.close()

print(n)
#print(os.path.exists("test.txt"))
print(os.path.exists("Day1w"))