text = "Cientista de dados eh a profissao que mais tem crescido em todo o mundo. \n"
text = text + "Esses profissionais precisam se especializar em programacao, estatistica e machine learning.\n"
text += "E claro, em Big Data."

with open("files/cientistas.txt", "r") as file:
    data = file.read()

print(len(data))
print(data)

with open("files/cientistas.txt", "w") as file:
    file.write(text[:21])
    file.write("\n")
    file.write(text[:33])

file = open("files/cientistas.txt", "r")
data = file.read()
file.close()

print(data)