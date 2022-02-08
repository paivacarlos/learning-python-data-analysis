# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos,
# adicione 2 elementos a lista e imprima a lista

myCountryList = ["Uruguay", "Brazil", "Chile", "Argentina"]

def addCountry(list, element1, element2):
    list.append(element1)
    list.append(element2)
    return print(list)

addCountry(myCountryList, "Colombia", "Paraguai")