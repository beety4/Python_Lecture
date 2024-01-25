class Person:
    name = ""
    age = 0

    def __init__(self):
        print("a")

    def __str__(self):
        return f"이름 : {self.name}, 나이 : {self.age}"


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age


c1 = Student("김철수", 17)
print(c1)