def fahrenheit(t):
    return ((float(9)/5) * t + 32)

def celsius(t):
    return ((float(9)/5) * t - 32)

#Criando uma lista
temperatures = [0, 22.5, 40, 100]

#Aplicando a funcao a cada elemento da lista temperatures
#em python 3 a funcao map() retronara um iterator
#logo precisaremos converter esse resulta em um lista
print(list(map(fahrenheit, temperatures)))

#usando o laço de repetição para imprimir o resultado da func map()
for temp in map(fahrenheit, temperatures):
    print(temp)

#somando os elemntos de tres listas
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10, 11, 12]

print(list(map(lambda x,y,z:x+y+z, l1, l2, l3)))