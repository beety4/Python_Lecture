class Person:
    name = ""
    age = 0
    def __str__(self):
        return f"이름 : {self.name} / 나이 : {self.age}"

class Student(Person):
    number = 0
    def __str__(self):
        return f"이름 : {self.name} / 나이 : {self.age} / 학번 : {self.number}"


c1 = Student()
c1.name = "김철수"
c1.age = 23
c1.number = 1001
print(c1)

