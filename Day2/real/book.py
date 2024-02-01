class Book:
    title = ""
    isbn = 0
    author = ""
    publisher = ""
    readPage = 0

    def __init__(self, title, isbn, author, publisher):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.publisher = publisher

    def read(self, nowPage):
        self.readPage = nowPage

    def __str__(self):
        return f"현재 읽은 페이지는 {self.readPage} 입니다."


book1 = Book("파이썬", 1001, "김민호", "세명컴고")
book2 = Book("JAVA", 1002, "김민호", "인하공전")

# print(book1)
# print(book2)

book1.read(5)
print(book1)
print(book2)

