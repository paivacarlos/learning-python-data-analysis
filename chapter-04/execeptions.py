#utilizando o trey/except

try:
    28 + 'c'
except TypeError:
    print("Operation Not permit!")

#utilizando o try, except e o else:
try:
    file = open("files/errortest.txt", "w")
    file.write("Wrinting in the file")
except IOError:
    print("Error: The file not found or can be read.")
else:
    print("Data registered with sucess!")
    file.close()
finally:
    print("Commands finally executed with sucess!")

def askingInt():
    while True:
        try:
            value = int(input("Digit a number: "))
        except:
            print("Sorry! You NEED to digit a number!")
            continue
        else:
            print("Tnhks for digited da number!")
            break
        finally:
            print("Thank you!!!")

askingInt()