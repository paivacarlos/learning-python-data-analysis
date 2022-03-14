list_num = ['Data', 'Science', 'Academy', 'Nota', 8.9, 2.8]

#A lista list_num é um objeto, uma instancia da classe lista em python
print(type(list_num))

#numero de vezes que aparece o numero desejado dentro da lista
print(list_num.count(8.9))

#criando um objeto chamado Car
class Car(object):
    pass
#instancia de Car
Volvo = Car()
print(type(Volvo))

#Criando uma classe
class Student:
    def __init__(self, name, age, scount):
        self.name = name
        self.age = age
        self.scount = scount

#criando um objeto stundet1 a patir da classe Stundent
stundent1 = Student("Carlos Adolfo", 11, 8.9)

#Atributo da classe Stundent, utilizado por cada objeto criado a partir desta classe
print(stundent1.name)
print(stundent1.age)
print(stundent1.scount)

