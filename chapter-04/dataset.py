fileCsv = open("files/Current_Employee_Names__Salaries__and_Position_Titles.csv", "r")
data = fileCsv.read()
rows = data.split("\n")
print(rows)

fullData = []
for row in rows:
    splitRow = row.split(",")
    fullData.append(splitRow)
    firstRow = fullData[0]

print(fullData)
print(len(fullData))

count = 0
for colum in firstRow:
    count = count + 1

print(count)
