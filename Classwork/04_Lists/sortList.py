import random

numList = []


def listGen(listIn,amount):
    for lp in range(amount):
        listIn.append(random.randint(0, 21))
        lp += 1


def compareNum(listIn):
    holdNum = 0
    checkNum = 1
    for lpv in range(len(listIn) - 1):
        num1 = listIn[holdNum]
        num2 = listIn[checkNum]
        if num2 < num1:
            lowestNum = listIn[checkNum]
            holdNum = checkNum
            checkNum += 1
        else:
            checkNum += 1
        lpv += 1
    return lowestNum


listGen(numList,50)
print(numList)
print(compareNum(numList), "Is the lowest")