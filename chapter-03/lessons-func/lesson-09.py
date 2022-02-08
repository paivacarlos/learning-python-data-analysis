# Exercício 9
# Abaixo você encontra a importação do Pandas,
# um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis.
# Um deles você vai usar no próximo exercício.
import pandas as pd
#print(dir(pd))

listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)

