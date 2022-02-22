def verificationOdd(number):
    if(number % 2 == 0):
        return True
    else:
        return False

lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(verificationOdd, lists)))
print(list(filter(lambda num: num > 6, lists)))