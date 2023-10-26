from pyperclip import *
#https://nostarch.com/contactus/
def titleCase():
    returnString = ""
    noCap = ['a', 'and', 'as', 'at', 'but', 'by', 'down', 'for', 'from', 'if', 'in', 'into', 'like', 'near', 'nor', 'of', 'off', 'on', 'once', 'onto', 'or', 'over', 'past', 'so', 'than', 'that', 'to', 'upon', 'when', 'with', 'Yet']
    stringList = []
    stringList += paste().split()
    for lp in range(0,len(stringList),1):
        if(lp == 0):
            temp = stringList[lp]
            if not temp.istitle():
                num = ord(temp[0])
                num -= 32
                temp = chr(num) + temp[1:]
            stringList[lp] = temp
        else:
            if(lp == len(stringList)-1):
                temp = stringList[lp]
                if not temp.istitle():
                    num = ord(temp[0])
                    num -= 32
                    temp = chr(num) + temp[1:]
                stringList[lp] = temp
            else:
                temp = stringList[lp]
                if not stringList[lp].lower() in noCap:
                    if not temp.istitle():
                        num = ord(temp[0])
                        num -= 32
                        temp = chr(num) + temp[1:]
                else:
                    num = ord(temp[0])
                    num += 32
                    temp = chr(num) + temp[1:]
                stringList[lp] = temp
        returnString += stringList[lp] + " "
        copy(returnString)
    return returnString

print(titleCase())