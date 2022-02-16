import json
from urllib.request import urlopen
import os

#Criando um dicionario
dict = {"name": "Carlos Paiva",
        "lenguage": "Python",
        "similar": ["C", "Modula-3", "lisp"],
        "user": 205215022022}

#Converter um dicionario em objeto json
#print(json.dumps(dict))

#Criar arquivo json
with open("files/data.json", "w") as file:
        file.write(json.dumps(dict))

#Leitura do arquivo json
with open("files/data.json", "r") as file:
        text = file.read()
        data = json.loads(text)

print(data)
print(data["similar"])

#Imprimir um arquivo json copiado da internet
response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
data = json.loads(response)[0]

print("Title:", data["title"])
print("URL: ", data["url"])
print("Duration: ", data["duration"])
print("Number of views: ", data["stats_number_of_plays"])

#Copiar conteudo de um arquivo para outro
file_source = "files/data.json"
file_destiny = "files/jason_data.txt"

#metodo 1
with open(file_source, "r") as infile:
        text = infile.read()
        with open(file_destiny, "w") as outfile:
                outfile.write(text)

#metodo 2
open(file_destiny, "w").write(open(file_source, "r").read())

#Leitura de arquivos json
with open("files/jason_data.txt", "r") as file:
        text = file.read()
        data = json.loads(text)

print(data)

