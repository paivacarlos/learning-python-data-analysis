#Retornar cada caracter em uma sequencia de caracteres
lista = [character for character in "Python is good!"]
print(lista)
print(type(lista))

#Retornar rais quadrada de cada elemento
lista2 = [number ** 2 for number in range(0, 11)]
print(lista2)

#Retornar apenas numeros pares
lista3 = [number for number in range(0, 11) if number % 2 == 0]
print(lista3)

#converter celsius para fahrenheit
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((float(9)/5) * temp + 32) for temp in celsius]
print(fahrenheit)

#operações aninhadas
lista4 = [x ** 2 for x in [x ** 2 for x in range(0, 11)]]
print(lista4)


