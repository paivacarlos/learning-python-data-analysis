expression1 = True
expression2 = False

if(expression1):
    print("Normal condition")


if(expression2):
    print("Go ahead because this expression is false")
elif(expression1):
    print("Second expression is true")

if(expression2):
    print("Go ahead because this expression is false")
elif(expression2):
    print("Second expression is true")
else:
    print("When the first and second expression is false")