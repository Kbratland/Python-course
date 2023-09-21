import time
import random

loopCode = True
diSource = "0"
diSpace = " "
diamondWidth = int(0)
start = "\033[1m"
end = "\033[0;0m"

while loopCode == True:

    randomBool = False
    diSpace = " "
    diSource = "0"
    getInput = True
    time.sleep(0.00015)

    while (getInput == True):

        print("\nI am going to draw a diamond, please enter a positive integer (Numbers over 150 will wrap, numbers over 190 will break diamond)\n" + end)
        try:
            diamondWidth = int(input())
            getInput == False
            if diamondWidth <= 0:

                print("\nThe number has to be above zero, try again\n" + end)
                continue
            if (diamondWidth % 2 != 0):

                startInt = 0
                isOdd = True
            else:
                isOdd = False
                startInt = 1
        except:

            time.sleep(0.00015)

            print("\nThats not a positive even integer, lets try again \n" + end)
            continue

        time.sleep(0.00015)
        print("\nEnter a character to make the diamond out of (Single characters preferred but not necessary)\n" + end)

        try:

            diIn = str(input())

            if diIn.lower() == "random":

                randomBool = True
                diSource = "0"

            else:

                diSource = diIn
        except:
            time.sleep(0.00015)
            print("\nThat doesn't work, lets try this again from the beginning\n" + end)
            continue
        diSpace = str(
            input("\nWhat should i make the spaces out of? \n\n" + end))
        if len(diSpace) != 1:
            print("\nYou can only use one character for spaces, lets try again\n" + end)
            continue
        else:
            break

    time.sleep(0.00015)
    print("\nPrinting\n" + end)

    level = 1
    widthIn = int(diamondWidth)

    for lp in range(startInt, diamondWidth, 2):

        if level <= diamondWidth:

            level += 1
            for lp2 in range(int(diamondWidth - level)):

                time.sleep(0.00015)
                if randomBool == True:

                    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
                    print(randomLowerLetter + end, end="")
                else:
                    print(diSpace + end, end="")

            for lp3 in range(int(lp)):

                time.sleep(0.00015)
                if randomBool == True:
                    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
                    print(randomUpperLetter + start, end="")
                else:
                    print(diSource + start, end="")

            for lp4 in range(int(diamondWidth - level)):

                time.sleep(0.00015)

                if randomBool == True:

                    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
                    print(randomLowerLetter + end, end="")
                else:
                    print(diSpace + end, end="")
            time.sleep(0.00015)

            print("")

    diamondWidth -= 1

    for lp in range(diamondWidth, 0, -2):

        if level <= diamondWidth: 

            level -= 1
            for lp2 in range(int(diamondWidth - level)):

                time.sleep(0.00015)
                if randomBool == True:

                    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
                    print(randomLowerLetter + end, end="")
                else:

                    print(diSpace + end, end="")

            for lp3 in range(int(lp)):

                time.sleep(0.00015)

                if randomBool == True:

                    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
                    print(randomUpperLetter + start, end="")
                else:

                    print(diSource + start, end="")

            for lp4 in range(int(diamondWidth - level)):

                time.sleep(0.00015)
                if randomBool == True:
                    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
                    print(randomLowerLetter + end, end="")
                else:
                    print(diSpace + end, end="")

            time.sleep(0.00015)

            print("")

    time.sleep(0.00015)
    print("\n All Done!, Type exit to exit or loop to run again\n" + end)
    randomBool = False
    responding = True

    while responding == True:

        try:

            responseInput = str(input().lower())

            if ("exit" in responseInput):

                print("\nGoodbye\n" + end)
                loopCode = False
                break

            elif ("loop" in responseInput):

                print("\nOk, Looping\n" + end)
                responding = False
                break
            else:

                print("\nThats not a response I can handle, lets try that again\n" + end)
                continue
        except:

            print("\nThats not a response I can handle, lets try that again\n" + end)
            continue
