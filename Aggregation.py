class Book:
    def get_title(self):
        return "Computer Science 3"

class Library:
    def __init__(self, external_book):
        self.book = external_book 

my_book = Book()
city_library = Library(my_book)

print(my_book.get_title())
print(city_library.book.get_title())
