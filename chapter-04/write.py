#Definindo o arquivo que será lido.
myFile = open("files/file-01.txt", "w")

#Gravando no arquivo
myFile.write("Testando gravacao de arquivos Python")

#Lendo o arquivo gravado
myFile = open("files/file-01.txt", "r")
print(myFile.read())

#Acrescentando conteudo
myFile = open("files/file-01.txt", "a")
myFile.write(" Acrescentando conteudo no arquivo")
myFile = open("files/file-01.txt", "r")
print(myFile.read())