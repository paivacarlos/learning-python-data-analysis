PilotsList = ["Senna", "Schumacher", "Hamilton", "Barrichelo", "Hill", "Frentzen"]

PilotsList[5] = "Coulthard"

print("Print a list with new pilot",PilotsList)

del PilotsList[5]

print("Print a list without the last pilot = ", PilotsList)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix: ", matrix)

list1_and_pos2 = matrix[1][2]
print("Print the number of list zero and position two: ", list1_and_pos2)

print("Looking for a value inside the list: ", 7 in matrix[2])

print("Lenght of the list: ", len(PilotsList))
print("Return the max value: ", max(matrix[2]))
print("Return the min value: ", min(matrix[2]))

PilotsList.append("Fisichella")
print("Add values in the list", PilotsList)

PilotsList.insert(1, "Trulli")
print("Add a value in the specification position of the list: ", PilotsList)

PilotsList.reverse()
print("Print a reverse list: ", PilotsList)