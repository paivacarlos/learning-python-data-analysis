# Exercício 4 - Crie uma função que receba um argumento formal e
# uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def elements(elemnt, *vartuple):
    print(elemnt)

    for i in vartuple:
        print(i)

elements("Formal element")
elements("Horse", "Red", "Love", "Ice", "Fire")