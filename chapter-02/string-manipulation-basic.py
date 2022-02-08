text = "Python data anaylise"

cont = 0
for i in text:
    if(text[cont] == "a"):
        print("Position = ", cont, " - ", i)
    cont += 1

print("Otherwise = ", text[::-1])
print("Two in Two = ", text[::2])
print("Count function: ", text.count('a'))
print(("Find a position: i ", text.find('i')))