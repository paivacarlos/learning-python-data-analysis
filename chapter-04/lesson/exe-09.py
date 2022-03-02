# Exercício 9 - Considere os dois dicionários abaixo.
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

print(dict1)
print(dict2)

dictResult = dict(list(map(lambda x,y: [x[0], y] , dict1, dict2.values())))
print("Result: ", dictResult)