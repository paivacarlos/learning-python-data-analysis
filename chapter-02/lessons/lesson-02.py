#Create a list with FIVE objects and print them.

class lessonClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

lessonList = []

lessonList.append(lessonClass("Carlos", 33))
lessonList.append(lessonClass("Patricia", 29))
lessonList.append(lessonClass("Fabricio", 28))

for obj in lessonList:
    print(obj.name, " | ", obj.age)