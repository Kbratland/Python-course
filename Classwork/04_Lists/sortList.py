import random

numList = []


def listGen(amount):
    for lp in range(amount):
        numList.append(random.randint(-10, 10))
        lp += 1


def compareNum():
    holdNum = 0
    checkNum = 1
    for lpv in range(len(numList) - 1):
        num1 = numList[holdNum]
        num2 = numList[checkNum]
        if num2 < num1:
            lowestNum = numList[checkNum]
            holdNum = checkNum
            checkNum += 1
        else:
            checkNum += 1
        lpv += 1
    return lowestNum


listGen(50)
print(numList)
print(compareNum(), "Is the lowest")
