#Defindo uma função
def firstFunc():
    print("Hello python world!")

firstFunc()

#Definindo uma função com parametro
def nameFunc(firstName, lastName):
    print("My name is %s %s" %(firstName, lastName))

nameFunc("Carlos", "Paiva")

#Função para somar némeros
def somFunc(firstNumber, secondNumber):
    print("First number: ", firstNumber)
    print("Second number: ", secondNumber)

    result = firstNumber + secondNumber
    print("Result is = ", result)

somFunc(28, 89)