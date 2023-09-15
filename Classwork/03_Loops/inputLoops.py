import time
isNum = False
failCount = 0
while isNum == False:
    userNumber = input("\nEnter a number please: ")
    try:
        userNumber = int(userNumber)
        isNum = True
    except:
        print("\nThats not a number\n")
        failCount += 1
if failCount == 0:
    print("\nwow first try")
else:
    print(f"\nNice! you took {failCount + 1} attempts to get it right")
    