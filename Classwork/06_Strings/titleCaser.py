from pyperclip import *

def titleCase():
    returnString = ""
    stringList = []
    stringList += paste().split()
    for lp in range(0,len(stringList),1):
        if(lp == 0):
            temp = stringList[lp]
            if not temp.istitle():
                num = ord(temp[0])
                num -= 32
                print(num)
                temp = chr(num) + temp[1:]
            stringList[lp] = temp
        else:
            if(lp == len(stringList)-1):
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
        returnString += stringList[lp] + " "
    return returnString

print(titleCase())