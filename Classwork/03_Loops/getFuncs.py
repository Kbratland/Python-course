rangeTop = input("Set max number: ")
rangeBot = input("Set min number: ")

def getInt(promptIn):
    while True:
        intIn = input(promptIn)
        try:
            intIn = int(intIn)
            if intIn <= rangeTop and intIn >= 0:
                return f"\nCorrect! The number {intIn} is an integer within the {rangeBot}-{rangeTop} range\n"
            else:
                print(f"\nThats not inside the {rangeBot}-{rangeTop} range, try again")  
                continue  
        except:
            print("\nThat is not a integer, try again")
            continue
        
def getFloat(promptIn):
    while True:
        floatIn = input(promptIn)
        try:
            floatIn = float(floatIn)
            if floatIn <= rangeTop and floatIn >= 0:
                return f"\nCorrect! The number {floatIn} is an float within the {rangeBot}-{rangeTop} range\n"
            else:
                print(f"\nThats not inside the {rangeBot}-{rangeTop} range, try again")
                continue
        except:
            print("\nThat is not a float, try again")
            continue
            
print(getInt(f"\nPlease enter a number in the {rangeBot}-{rangeTop} range: "))
print(getFloat(f"\nPlease enter a float in the {rangeBot}-{rangeTop} range: "))