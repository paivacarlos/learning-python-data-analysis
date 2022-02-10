#Importando o pacote OS - manipula o sistema operacional
import os

text = "Cientista de dados eh a profissao que mais tem crescido em todo o mundo. \n"
text = text + "Esses profissionais precisam se especializar em programacao, estatistica e machine learning.\n"
text += "E claro, em Big Data."

print(text)

#Criando o arquivo
fileCreated = open(os.path.join("files/cientistas.txt"), "w")

#Gravando os dados no arquivo
for word in text.split():
    fileCreated.write(word + " ")

#fechando o arquivo
fileCreated.close()

#lendo o arquivo
fileToRead = open("files/cientistas.txt", "r")
data = fileToRead.read()
fileToRead.close()

print(data)