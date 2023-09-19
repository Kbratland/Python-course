def getInt(promptIn):
    while True:
        intIn = input(promptIn)
        try:
            intIn = int(intIn)
            if intIn <= 100 and intIn >= 0:
                return f"\nCorrect! The number {intIn} is an integer within the 1 - 100 range\n"
            else:
                print("\nThats not inside the 1 - 100 range, try")  
                continue  
        except:
            print("\nThat is not a integer, try again")
            continue
        
def getFloat(promptIn):
    while True:
        floatIn = input(promptIn)
        try:
            floatIn = float(floatIn)
            if floatIn <= 100 and floatIn >= 0:
                return f"\nCorrect! The number {floatIn} is an float within the 1 - 100 range\n"
            else:
                print("\nThats not inside the 1 - 100 range, try")
                continue
        except:
            print("\nThat is not a float, try again")
            continue
            
print(getInt("\nPlease enter a number in the 1-100 range: "))
print(getFloat("\nPlease enter a float in the 1-100 range: "))