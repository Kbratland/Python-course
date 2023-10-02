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


def quickSort(listIn,lowIndex,highIndex,pivotIndex):
    pivot = pivotIndex
    lowIn = lowIndex
    highIn = highIndex
    print(f"\nStart high is {highIn} (value is {listIn[highIn]}), start low is {lowIn} (value is {listIn[lowIn]}), start pivot is {pivot} (value is {listIn[pivot]})")
    print(listIn,"\n")
    goingUp = True
    swap = True
    while swap:
        print(f"\nHigh is {highIn} (value is {listIn[highIn]}),  low is {lowIn} (value is {listIn[lowIn]}),  pivot is {pivot} (value is {listIn[pivot]})")
        print("\n",listIn)
        if goingUp:
            
            if listIn[pivot] > listIn[highIn]:
                print("changing direction")
                (listIn[pivot],listIn[highIn]) = (listIn[highIn],listIn[pivot])
                if highIn == pivot:
                    swap = False
                pivot = highIn
                lowIn +=1
                goingUp = False
            else:
                highIn -= 1
        else:
            
            if listIn[pivot] < listIn[lowIn]:
                print("changing direction")
                (listIn[pivot],listIn[lowIn]) = (listIn[lowIn],listIn[pivot])
                if lowIn == pivot:
                    swap = False
                pivot = lowIn
                highIn -=1
                goingUp = True
            else:
                lowIn +=1
    print(f"\nEnd high is {highIn} (value is {listIn[highIn]}), end low is {lowIn} (value is {listIn[lowIn]}), end pivot is {pivot} (value is {listIn[pivot]})")
    print(listIn)

listGen(numList,25)
print(quickSort(numList,0,len(numList)-1,0))
# print("\nOriginal List:",numList)
# print("\nThe sorted list is:",sortList(numList))
