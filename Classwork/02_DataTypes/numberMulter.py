import time

time.sleep(0.25)

print("\nHello, please give me number to multiply (Now accepting floats!)")

time.sleep(0.25)

numVar = float(input("Number: "))
numMult = float(input("Multiply by:"))
numResult = round((numVar * numMult),6)

time.sleep(0.15)

print(f"The number {numVar} multiplied by {numMult} is {numResult}\n")

time.sleep(0.25)