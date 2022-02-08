# Exercício 7 - Crie uma lista vazia e uma variável com valor 4.
# Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

emptyList = []
value = 4

for i in range(0, 21):
    if(value <= 20):
        if(i % 2 == 0):
            emptyList.append(i)

print(emptyList)