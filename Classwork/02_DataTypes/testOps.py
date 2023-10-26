import pyperclip

templist = []
templist += str(pyperclip.paste()).split()
for lp in range(len(templist)-1):
    temp = templist[lp]
    num = ord(temp[0])
    num += 32
    temp = chr(num) + temp[1:]
    templist[lp] = temp
print(templist)