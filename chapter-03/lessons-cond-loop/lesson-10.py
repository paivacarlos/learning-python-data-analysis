# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo.
# Use um placeholder na sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade;
# se ela não é tão brilhante como os sonhos, tem pelo menos a
# vantagem de existir.” (Machado de Assis)

phrase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
appearLetter = "r"
count = 0

for i in phrase:
    if(i == appearLetter):
        count += 1

print("Na frase: %s A letra 'r' aparece %r vezes." %(phrase, count))