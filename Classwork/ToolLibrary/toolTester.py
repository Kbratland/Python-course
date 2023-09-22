from swagFuncs import *
while True:      
    mainChoice = int(input("\nChoose a function, 1 for getInt, 2 for getFloat, 3 for checkPrime, 4 for checkPrime with prints: "))
    if mainChoice == 1:
        print(getInt("(getInt) Enter a integer: "))
    if mainChoice == 2:
        print(getFloat("(getFloat) Enter a float: "))
    if mainChoice == 3:
        print(checkPrime("(checkPrime) Enter a integer: "))
    if mainChoice == 4:
        print(checkPrime("(checkPrime) Enter a integer: ",True))