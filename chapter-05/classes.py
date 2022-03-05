class Book():
    def __init__(self):
        self.title = "The Da Vince Code"
        self.isbn = "11222"
        print("Constructor called to build a class!")

    def prints(self):
        print(f"The created is {self.title} and ISBN {self.isbn}.")

book1 = Book()
#print(type(book1))

#imprimindo o atributo do objeto
print(book1.title)

#imprimindo o metodo do objeto
book1.prints()