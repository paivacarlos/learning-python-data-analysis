#Importando a funcao reduce do pacoto functools
from functools import reduce

#Criando a lista
list = [10, 20, 30, 40, 50]

def som(a,b):
    result = a + b
    return result

#Usando o reduce com uma funcao e uma lista. A funcao vai retornar o valor maximo
print(reduce(som, list))

#Usando o reduce com lambda
print(reduce(lambda x,y: x+y, list))

#Podemos atribuir a expressao lambda a uma variavel
maxFind = lambda a,b: a if(a > b) else b
print(type(maxFind))

#reduzindo a lista até o valor maximo, atraves da funcao criada na expressao lambda
print(reduce(maxFind, list))