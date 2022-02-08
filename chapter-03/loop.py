#tupla
tp = ("Uruguay", "Argentina", "Chile", "Brasil")
for country in tp:
    print(country)

#list
list1 = ["milk", "tomato", "lettuce"]
for vegetables in list1:
    if(vegetables == "lettuce"):
        print(vegetables)

#range
for i in range(0, 100, 10):
    print(i)

#matrix
for i in range(0, 5):
    for a in range(0, 5):
        print(i, a )

#key and value
dic = { 'k1': 'Porto Alegre', 'k2': 'São Leopoldo', 'k3': 'Cachoeirinha'}
for k,v in dic.items():
    print(k, v)

