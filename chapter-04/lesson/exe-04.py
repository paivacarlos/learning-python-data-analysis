# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def funcSrt(value):
    return pow(value, 2)

def funCube(value):
    return pow(value, 3)

print(list(map(lambda i: [funcSrt(i), funCube(i)], lista)))
