import time
isNum = False
attemptCount = 1
standard_input = 0
while isNum == False:
    userInput = input("\nEnter a number please, or type q to quit: ")
    try:
        userInput = int(userInput)
        isNum = True
    except:
        if userInput.lower() == "q":
            print("\nGoodbye\n")
            exit()
        time.sleep(0.015)
        print("\n Thats not a number")
        attemptCount += 1
        if attemptCount > 15:
            time.sleep(0.015)
            print("\nThis isn't going anywhere, goodbye\n")
            exit()
if attemptCount == 1:
    time.sleep(0.015)
    print("\nWow first try!\n")
else:
    time.sleep(0.015)
    print(f"\nNice! you took {attemptCount} attempts to get it right\n")
