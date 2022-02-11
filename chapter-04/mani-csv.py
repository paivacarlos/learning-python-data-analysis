import csv

with open("files/numbers.csv", "w", newline='') as myCsvFile:
    writer = csv.writer(myCsvFile)
    writer.writerow(("First", "Second", "Third"))
    writer.writerow((28, 89, 1))
    writer.writerow((22, 42, 33))

#Leitura do arquivo csv
with open("files/numbers.csv", "r") as file:
    reader = csv.reader(file)
    for i in reader:
        print("Number of columns: ", len(i))
        print(i)

#Gerando uma lista com os dados do arquivo csv
with open("files/numbers.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader) #o que converte em lista

print(data)

#Imprimindo a partir de uma segunda linha
for line in data[2:]:
    print("line: ", line)