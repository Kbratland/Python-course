import time
isNum = False
attemptCount = 1
while isNum == False:
    userInput = input("\nEnter a number please: ")
    try:
        userInput = int(userInput)
        isNum = True
    except:
        time.sleep(0.015)
        print("\n Thats not a number\n")
        attemptCount += 1
        if attemptCount > 10:
            time.sleep(0.015)
            print("\nThis isn't going anywhere, goodbye\n")
            exit()
if attemptCount == 0:
    time.sleep(0.015)
    print("\nwow first try")
elif attemptCount <= 10:
    time.sleep(0.015)
    print(f"\nNice! you took {attemptCount} attempts to get it right")
    