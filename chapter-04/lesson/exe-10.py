# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for indexOfTheList, valueOfTheList in enumerate(lista):
    if(indexOfTheList > 5):
        print(indexOfTheList, valueOfTheList)