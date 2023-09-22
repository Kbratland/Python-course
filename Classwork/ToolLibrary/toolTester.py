from swagFuncs import *

mainChoice = int(input("\nChooose a function, 1 for getInt, 2 for getFloat, 3 for checkPrime: "))
if mainChoice == 1:
    print(getInt("(getInt) Enter a integer: "))
if mainChoice == 2:
    print(getFloat("(getFloat) Enter a float: "))
if mainChoice == 3:
    print(checkPrime("(checkPrime) Enter a integer: "))