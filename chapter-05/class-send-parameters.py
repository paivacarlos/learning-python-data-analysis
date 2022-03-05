class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        print("Constructor called to build a class!")

    def prints(self):
        print(f"The created is {self.title} and ISBN {self.isbn}.")

book = Book("The french revolution", 1010898928)
print(book.title)
book.prints()

class Dog():
    def __init__(self, family):
        self.family = family
        print("Constructor called to build a class!")

billy = Dog("buldog")
louis = Dog("border")

print(billy.family)
print(louis.family)


