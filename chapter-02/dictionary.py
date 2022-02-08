DicFootballPlayers = {"Ronaldinho Gaúcho": 10, "Raul": 7, "Ronaldo": 9, "Beckham": 23}

print(DicFootballPlayers)
print("Print the index of dictionary: ", DicFootballPlayers["Raul"])

DicFootballPlayers["Kaka"] = 22
print("Add a new element and value", DicFootballPlayers)
print("Lenght of the Dictionary: ", len(DicFootballPlayers))
print("Print the Key value: ", DicFootballPlayers.keys())
print("Print the values: ", DicFootballPlayers.values())
print("Print the items, wich key/value: ", DicFootballPlayers.items())

DicFootballPlayers2 = {"Falcao": 5, "Pirlo": 42}
DicFootballPlayers.update(DicFootballPlayers2)
print("Print the update of dictionary: ", DicFootballPlayers)

DicOfLists = {"key1": 1020, "Key2":["Joao", "Maria", "Jose"], "key3":[10,20,30]}
print("Print the list of dictionary", DicOfLists)

DicOfDics = {"ke1": {"key2nestle":{"key3nestle": "dic nestled!"}}}
print("Print a dictionary nestled: ", DicOfDics)