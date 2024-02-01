import os

with open("test.txt", 'r') as f:
    a = f.readline()
    print(a)

b = os.path.exists("test.txt")
print(b)
try:
    os.remove("test.txt")
except:
    pass

os.makedirs("folder")
os.rmdir("folder")

