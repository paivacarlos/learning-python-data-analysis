#Definindo o arquivo que será lido.
myFile = open("files/file-01.txt", "r")

#Lendo o arquivo
print(myFile.read())

#Contar o numero de caracteres
print(myFile.tell())

#Retornar para o inicio do arquivo
print(myFile.seek(0,0))

#Ler os primieros 10 caracteres
print(myFile.read(10))