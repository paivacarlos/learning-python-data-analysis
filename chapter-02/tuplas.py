Tupla1 = ("Siberia", 22, "Dan Brown")
print("Print a tupla: ", Tupla1)
print("Print a value of Index position: ", Tupla1[2])
print("Print a lenght od Tupla: ", len(Tupla1))
print("Print using a slicing like list: ", Tupla1[1:])
print("Print a index position: ", Tupla1.index("Dan Brown"))

Tupla2 = ("A", "B", "C")
print("Print a second tupla: ", Tupla2)

list1 = list(Tupla2)
list1.append("D")
Tupla3 = tuple(list1)
print("Print a tuple converted: ", Tupla3)