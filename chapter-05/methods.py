#Cirando a classe Circle
class Circle():
    pi = 3.14

    #Quando um objeto desta classe for criado, este método será executado e o valor do raio será 5.
    def __init__(self, rain = 5):
        self.rain = rain

    #Esse metodo calcula a área, self utiliza os atributos deste mesmo objeto
    def area(self):
        return (self.rain * self.rain) * Circle.pi

    #Metodo para gerar um novo raio
    def setRain(self, new_rain):
        self.rain = new_rain

    #Metodo para obter o circulo
    def getRain(self):
        return self.rain

circle = Circle()

#executando um metodo da classe Circle
print(circle.getRain())

#imprimindo o valor da area
print(circle.area())