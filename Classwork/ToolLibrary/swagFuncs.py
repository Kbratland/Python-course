from random import *
from time import *
from pyperclip import *
from re import *


def titleCase():
    stringList = []
    stringList += paste().split()
    for lp in range(0, len(stringList), 1):
        if (lp == 0):
            temp = stringList[lp]
            if not temp.istitle():
                num = ord(temp[0])
                num -= 32
                print(num)
                temp = chr(num) + temp[1:]
            stringList[lp] = temp
        else:
            if (lp == len(stringList)-1):
                temp = stringList[lp]
                if not temp.istitle():
                    num = ord(temp[0])
                    num -= 32
                    print(num)
                    temp = chr(num) + temp[1:]
                stringList[lp] = temp
            else:
                if len(stringList[lp]) > 3:
                    temp = stringList[lp]
                    if not temp.istitle():
                        num = ord(temp[0])
                        num -= 32
                        print(num)
                        temp = chr(num) + temp[1:]
                    stringList[lp] = temp


def getInt(promptIn, minInt=None, maxInt=None):
    while True:
        intIn = input("\n" + str(promptIn))
        try:
            intIn = int(intIn)
            if minInt != None and intIn < minInt:
                sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minInt}")
                continue
            if maxInt != None and intIn > maxInt:
                sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxInt}")
                continue
            return f"\nYour number is accepted"
        except:
            sleep(0.15)
            print("\nThat is not a integer, try again")
            continue


def getFloat(promptIn, minFloat=None, maxFloat=None):
    while True:
        floatIn = input("\n" + str(promptIn))
        try:
            floatIn = float(floatIn)
            if minFloat != None and floatIn < minFloat:
                sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minFloat}")
                continue
            if maxFloat != None and floatIn > maxFloat:
                sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxFloat}")
                continue
            return f"\nYour number is accepted"
        except:
            sleep(0.15)
            print("\nThat is not a float, try again")
            continue


def checkPrime(promptIn, printTests=False):
    while True:
        sleep(0.15)
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
                    return False
                lp += 1
            return True
        except:
            print("\nThats not an integer, try again\n")
            continue


def listGen(listIn, amount, low=0, high=100):
    for lp in range(amount):
        listIn.append(randint(low, high))
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
    # 833 number sorted per second
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


def phoneEmailSearch():
    phoneRegex = compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', VERBOSE)

    emailRegex = compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', VERBOSE)

    text = str(paste())

    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        # copy('\n'.join(matches))
        return '\n'.join(matches)
    else:
        return('No phone numbers or email addresses found.')