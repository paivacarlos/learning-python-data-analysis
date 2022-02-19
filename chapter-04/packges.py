#Importando um modulo em Python
import math

#Verificando todos os metodos disponiveis no modulo
print(dir(math))

#metodos do modulo Math
print(math.sqrt(5))

#importando apenas um dos metodos do modulo Math
from math import sqrt

#usando o metodo importado
print(sqrt(9))

#help do metodo sqrt do modulo math
help(sqrt)

#importando o pacote random
import random
print(random.choice(["Chevrolet", "Ford", "Fiat", "Citroen"]))
print(random.sample(range(100), 10))

#importantar o pacoto statistics
import statistics
data = [2.22, 89.9, 33.01, 80.90, 2828, 1002, 3]
print(statistics.mean(data))
print(statistics.median(data))

#importar pacote OS
import os
print(os.getcwd())
print(dir(os))

#importar o pacte sys
import sys
sys.stdout.write("Perrier\n")
print(sys.version)
print(dir(sys))

#importando o modulo request do pacote urllib, usado para trazer url's
import urllib.request

#variavel de resposta armazena o objeto de conexao a url passada por parametro
response = urllib.request.urlopen("http://python.org")
print(response)

#chamando o metodo read() do objeto resposta e armazenando o codigo html na variavel html
html = response.read()
print(html)


