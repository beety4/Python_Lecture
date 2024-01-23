class Book:
    title = ""
    isbn = 0
    author = ""
    readpage = ""

    def __init__(self, title, isbn, author):
        self.title = ""
        self.isbn = 0
        self.author = author

    def read(self, pageNo):
        self.readpage = pageNo

    def nowpage(self):
        print(f"읽은 페이지 : {self.readpage}")


bookInfo = Book("파이썬", 1001, "김저자")
print(type(bookInfo))
print(isinstance(bookInfo, Book))
bookInfo.read(4)
bookInfo.nowpage()

bookInfo.read(7)
bookInfo.nowpage()


