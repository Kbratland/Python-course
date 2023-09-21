import time


def getInt(promptIn, minInt=None, maxInt=None):
    while True:
        intIn = input(promptIn)
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
        floatIn = input(promptIn)
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


# time.sleep(0.15)
# print(getInt("Int, No limit "))
# time.sleep(0.15)
# print(getFloat("Float, No limit "))
# time.sleep(0.15)
# print(getInt("\nInt min 10 ", minInt=10))
# time.sleep(0.15)
# print(getFloat(f"\nFloat min 10 ", minFloat=10))
# time.sleep(0.15)
# print(getInt("\nInt max 10 ", maxInt=10))
# time.sleep(0.15)
# print(getFloat(f"\nFloat max 10 ", maxFloat=10))
# time.sleep(0.15)
# print(getInt("\nInt min 10, max 100 ", minInt=10, maxInt=100))
# time.sleep(0.15)
# print(getFloat(f"\nFloat min 10 ", minFloat=10, maxFloat=100))
