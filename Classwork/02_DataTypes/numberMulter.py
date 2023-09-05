import time

time.sleep(0.25)

print("\nHello, please give me number to multiply (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("Number: "))
except:
    print("Thats not a number, Goodbye")
    exit()
try:
    numMult = float(input("Multiply by:"))
except:
    print("thats not a number, Goodbye")
    exit
numResult = round((numVar * numMult),6)

time.sleep(0.15)

print(f"The number {numVar} multiplied by {numMult} is {numResult}")

time.sleep(0.25)