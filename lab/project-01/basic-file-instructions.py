import csv

def createCsvFile(directory, nameFile, data):
    dir = f"{directory}/{nameFile}"
    with open(dir, "w", newline='') as csvFile:
        row = len(data)
        print("ROW: ", row)
        if(row > 0):
            for i in data:
                writer = csv.writer(csvFile)
                writer.writerow((i))

def readCsvFile(directory, nameFile):
    dir = f"{directory}/{nameFile}"
    with open(dir, "r") as file:
        reader = file.read()
        data = reader.split("\n")
        dataList = list(data)
        for row in dataList:
            print(row)


firstSemester = "January", "February", "Mach", "April", "May"
secondSemester = "June", "July", "September", "Octuber", "November", "December"
years = "2022", "2023", "2024"

MyDataList = [[firstSemester], [secondSemester], [years]]

MyFileCsv = createCsvFile("csvFiles", "exemplo-01", MyDataList)
readCsvFile("csvFiles", "exemplo-01")


