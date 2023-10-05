import random
import time


def getInt(promptIn, minInt=None, maxInt=None):
    while True:
        intIn = input("\n" + str(promptIn))
        try:
            intIn = int(intIn)
            if minInt != None and intIn < minInt:
                time.sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minInt}")
                continue
            if maxInt != None and intIn > maxInt:
                time.sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxInt}")
                continue
            return f"\nYour number is accepted"
        except:
            time.sleep(0.15)
            print("\nThat is not a integer, try again")
            continue


def getFloat(promptIn, minFloat=None, maxFloat=None):
    while True:
        floatIn = input("\n" + str(promptIn))
        try:
            floatIn = float(floatIn)
            if minFloat != None and floatIn < minFloat:
                time.sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minFloat}")
                continue
            if maxFloat != None and floatIn > maxFloat:
                time.sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxFloat}")
                continue
            return f"\nYour number is accepted"
        except:
            time.sleep(0.15)
            print("\nThat is not a float, try again")
            continue


def checkPrime(promptIn, printTests=False):
    while True:
        time.sleep(0.15)
        numIn = input("\n" + str(promptIn))
        try:
            numIn = int(numIn)
            for lp in range(2, numIn):
                numDiv = lp
                numSub = numIn
                if printTests:
                    print(
                        f"Testing {numSub} % {numDiv}, result is {numSub % numDiv}")
                if numSub % numDiv == 0:
                    return f"\nThe number {numIn} is not prime\n"
                lp += 1
            return f"\nThe number {numIn} is prime\n"
        except:
            print("\nThats not an integer, try again\n")
            continue


def listGen(listIn, amount,low = 0,high = 100):
    for lp in range(amount):
        listIn.append(random.randint(low, high))
        lp += 1


def minNum(listIn):
    lowestNum = listIn[0]
    holdNum = 0
    checkNum = 1
    for lp in range(len(listIn) - 1):
        num1 = listIn[holdNum]
        num2 = listIn[checkNum]
        if num2 < num1:
            lowestNum = listIn[checkNum]
            holdNum = checkNum
            checkNum += 1
        else:
            checkNum += 1
        lp += 1
    return int(lowestNum)


def sortList(listIn):
    #833 number sorted per second
    tempList = []
    tempLen = len(listIn)
    lp = 0
    while lp < tempLen:
        tempNum = minNum(listIn)
        listIn.remove(tempNum)
        tempList.append(tempNum)
        lp += 1
    return tempList

def quickSort(listIn, lowIndex, highIndex, pivotIndex):
    pivot = pivotIndex
    lowIn = lowIndex
    highIn = highIndex
    goingUp = True
    swap = True
    while swap and highIn > lowIn:
        if goingUp:
            if listIn[pivot] > listIn[highIn]:
                (listIn[pivot], listIn[highIn]) = (
                    listIn[highIn], listIn[pivot])
                pivot = highIn
                lowIn += 1
                goingUp = False
            else:
                highIn -= 1
        else:

            if listIn[pivot] < listIn[lowIn]:
                (listIn[pivot], listIn[lowIn]) = (listIn[lowIn], listIn[pivot])
                pivot = lowIn
                highIn -= 1
                goingUp = True
            else:
                lowIn += 1

    if pivot > lowIndex:
        quickSort(listIn, 0, pivot-1, 0)
    if pivot < highIndex:
        quickSort(listIn, pivot+1, highIndex, pivot+1)
    else:
        print(listIn)
        # return listIn

numList = []
listGen(numList,20)
print(numList)
print(quickSort(numList, 0, len(numList)-1, 0))
