x = [1, 2, 3]
y = [4, 5, 6]

#Unindo as listas
print(list(zip(x,y)))

#Ter atencao com listas com tamanhos diferentes
print(list(zip("abcd", "xy")))

#Craindo dois dicionarios
dic1 = {"a":1, "b":2}
dic2 = {"c":3, "d":4}

print("Keys: ", list(zip(dic1, dic2)))
print("Values: ", list(zip(dic1.values(), dic2.values())))