def getInt(intIn):
    while True:
        try:
            intIn = int(intIn)
            if intIn <= 100 and intIn >= 0:
                return f"\nCorrect! The number {intIn} is an integer within the 1 - 100 range\n"
            else:
                return("\nThats not inside the 1 - 100 range, goodbye")    
        except:
            return("\nThat is not a integer, goodbye")
            
def getFloat(floatIn):
    while True:
        try:
            floatIn = float(floatIn)
            if floatIn <= 100 and floatIn >= 0:
                return f"\nCorrect! The number {floatIn} is an float within the 1 - 100 range\n"
            else:
                return("\nThats not inside the 1 - 100 range, goodbye")
        except:
            return("\nThat is not a float, goodbye")
            
while True:           
    print(getInt(input("\nPlease enter a number between 1 and 100: ")))
    print(getFloat(input("\nPlease enter a float between 1 and 100: ")))