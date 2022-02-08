#Faça uma calculadora.

def som(value1, value2):
    return value1 + value2

def sub(value1, value2):
    return value1 - value2

def mul(value1, value2):
    return value1 * value2

def div(value1, value2):
    if(value1 <= 0 or value2 <= 0):
        return print("Sorry! There is no number divisible by 0!")
    else:
        return value1 / value2

print("********** Python Calculator **********")
print("Select a number of option you wish:")
print(" ")
print("1 - SOM")
print("2 - Sub")
print("3 - Mul")
print("4 - Div")
print(" ")

optionDigited = input("Digit your option (1/2/3/4): ")
firstValueDigited = float(input("Please digit a first value: "))
secondValueDigited = float(input("Please digit a second value: "))

result = 0
operation = "null"

if(optionDigited == "1"):
    result = som(firstValueDigited, secondValueDigited)
    operation = "+"
    print("Aqui: ",result)
elif(optionDigited ==  "2"):
    result = sub(firstValueDigited, secondValueDigited)
    operation = "-"
elif(optionDigited == "3"):
    result = mul(firstValueDigited, secondValueDigited)
    operation = "*"
elif(optionDigited == "4"):
    result = div(firstValueDigited, secondValueDigited)
    operation = "/"
else:
    optionDigited = False
    result = print("Please send a option of Menu!")

if(firstValueDigited <= 0 or secondValueDigited <= 0):
    result
elif(optionDigited == False):
    result
else:
    print(firstValueDigited, " ", operation, " ", secondValueDigited, " ", " = ", result)
