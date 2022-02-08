# Exercício 6 - Crie uma variável chamada contador = 0.
# Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

counter = 0
valueToInterrupt = 23

for i in range(counter, 101):
    if(i == valueToInterrupt):
        break
    print(i)