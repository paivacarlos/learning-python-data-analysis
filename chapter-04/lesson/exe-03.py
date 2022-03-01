# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
print(matrix)
print("=======================//============================//======================")

firstColumn = list(map(lambda i:i[0], matrix))
secondColumn = list(map(lambda j:j[1], matrix))

columns = [firstColumn, secondColumn]
counter = 0
listsAux = []
listResult = []
for i in range(0, len(matrix)):
    listsAux = list(map(lambda line: line[counter], columns))
    listResult.append(listsAux)
    counter += 1

for i in listResult:
    print(i)