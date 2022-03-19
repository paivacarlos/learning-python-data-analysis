# Exercício 3 - Crie a classe Smartphone com 2 atributos,
# tamanho e interface e crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, size, interface):
        self.size = size
        self.interface = interface
        print("Smartphone created!")

class MP3Player(Smartphone):
    def __init__(self, capacity, size, interface):
        Smartphone.__init__(self, size, interface)
        print("Object Smartphone created!")
        self.capacity = capacity

    def __str__(self):
        return f"Tamanho: {self.size}, Interface: {self.interface}, Capacidade: {self.capacity}"

mp3 = MP3Player("6.0", "Android", "64gb")
print(mp3)