import time


def getInt(promptIn, minInt=None, maxInt=None):
    while True:
        intIn = input("\n" + str(promptIn))
        try:
            intIn = int(intIn)
            if minInt != None and intIn < minInt:
                time.sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minInt}")
                continue
            if maxInt != None and intIn > maxInt:
                time.sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxInt}")
                continue
            return f"\nYour number is accepted"
        except:
            time.sleep(0.15)
            print("\nThat is not a integer, try again")
            continue


def getFloat(promptIn, minFloat=None, maxFloat=None):
    while True:
        floatIn = input("\n" + str(promptIn))
        try:
            floatIn = float(floatIn)
            if minFloat != None and floatIn < minFloat:
                time.sleep(0.15)
                print(f"\n Your number is to small, the minimum is {minFloat}")
                continue
            if maxFloat != None and floatIn > maxFloat:
                time.sleep(0.15)
                print(f"\nYour number is to big, the maximum is {maxFloat}")
                continue
            return f"\nYour number is accepted"
        except:
            time.sleep(0.15)
            print("\nThat is not a float, try again")
            continue


def checkPrime(promptIn, printTests=False):
    while True:
        time.sleep(0.15)
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
                    return f"\nThe number {numIn} is not prime\n"
                lp += 1
            return f"\nThe number {numIn} is prime\n"
        except:
            print("\nThats not an integer, try again\n")
            continue
