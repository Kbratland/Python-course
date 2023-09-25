
import time

count = 0
foodCount = 0
nameList = []
going = True
while (going == True):
    print("Enter your name")
    nameHolder = input()
    time.sleep(0.15)
    if (nameHolder == "tally"):
        print(f"we counted {count} names!")
        break
    count += 1
    print("Hello", nameHolder)
    time.sleep(0.15)
    print("Whats your favorite food")
    checker = input()
    time.sleep(0.15)
    if (checker == "tally"):
        print(f"we asked for {count} names!")
        going = False
        break
    elif (checker == "cheese" or checker == "Cheese"):
        print("yum")
        foodCount += 1
    else:
        print("not cheese :( but still good")
        foodCount += 1
