list1 = ["Brazil", "Italy", "EUA"]
print(list(enumerate(list1)))

#IMprimindo os valores de uma lita com a funcao enumerate
for index, value in enumerate(list1):
    print(index, value)

list2 = [10, 20, 30, 40, 50]

for index, value in enumerate(list2):
    if(value > 28):
        break
    else:
        print(value)