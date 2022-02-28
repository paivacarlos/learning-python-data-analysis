# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
   print(i)

print(" ")
print("=====================//======================")
print((" "))
listAll = []
listUpper = []
listLower = []
listLenth = []

listUpper = list(map(lambda word:word.upper(), palavras))
listLower = list(map(lambda word:word.lower(), palavras))
listLenth = list(map(lambda word:len(word), palavras))

listAll = [listUpper, listLower, listLenth]


for i in range(0,len(palavras)):
    print(list(map(lambda w:w[i], listAll)))


#Função aprimorada:
resultado = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print (i)