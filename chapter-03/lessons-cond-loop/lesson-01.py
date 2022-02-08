# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

digitDay = input("Send a day of the week: ")
control = True

for day in week:
    control = True
    if(week[0] == digitDay):
        print("C'mon! Enjoin your Sunday!")
        break
    elif(week[6] == digitDay):
        print("C'mon! Enjoin your Saturday")
        break
    elif(day == digitDay):
        print("It's " + day + "! You have to work!")
        break
    else:
        control = False

if(control == False):
    print("Outlier Found!")
    print(digitDay + " - It's not a word of the week.")

