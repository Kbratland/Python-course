import random

numList = []


def listGen(listIn,amount):
    for lp in range(amount):
        listIn.append(random.randint(0, 11))
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
    tempList = []
    tempLen = len(listIn)
    lp = 0
    while lp < tempLen:
        tempNum = minNum(listIn)         
        listIn.remove(tempNum)
        tempList.append(tempNum)
        lp += 1
    return tempList


def quickSort(listIn,lowIndex,highIndex):
    pivot = lowIndex
    checkNum = highIndex
    if(listIn[pivot] < listIn[checkNum]):
        print(listIn)
        (listIn[pivot],)
        temp = pivot
        pivot = checkNum
        checkNum = temp + 1
        print(listIn)
    return listIn

listGen(numList,13)
quickSort(numList,0,len(numList))
# print("\nOriginal List:",numList)
# print("\nThe sorted list is:",sortList(numList))
