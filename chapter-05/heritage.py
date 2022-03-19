#Criando a classe Animal - Esta é a SUPER-CLASSE
class Animal():
    def __init__(self):
        print("Animal created!")
    def Identif(self):
        print("Animal")
    def Eat(self):
        print("Eating")

#Criando a classe Dog - Esta é a SUB-CLASSE
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Object Dog() created.")
    def Identif(self):
        print("dog")
    def Bark(self):
        print("au- au- au!")

#Criando um objeto, logo, estamos instanciando uma classe
billy = Dog()
billy

#Executando o metodo da SUB-CLASSE
billy.Identif()

#Executando o metodo da SUPER-CLASSE
billy.Eat()

#Executando o metodo da SUB-CLASSE
billy.Bark()