import random

numList = []


def listGen(listIn,amount):
    for lp in range(amount):
        listIn.append(random.randint(0, 21))
        lp += 1


def minNum(listIn):
    lowestNum = 0
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
    for lp in range(len(listIn) - 1):
        tempNum = minNum(listIn)
        print(f"Temp is {tempNum}")
        tempList.append(tempNum)
        listIn.remove(tempNum)
        lp += 1
    return tempList


listGen(numList,50)
print(numList)
print(sortList(numList))
