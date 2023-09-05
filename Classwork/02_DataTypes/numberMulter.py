import time
#-,+,*,/,%,//,**
time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is - (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar - numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} minus {numMult} is {numResult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is + (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\n Affect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar + numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} Added to {numMult} is {numResult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is * (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar * numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} multiplied by {numMult} is {numResult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is / (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar / numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} divided by {numMult} is {numResult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is % (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar % numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} is {numResult} percent of {numMult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is // (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar // numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} Divided by {numMult} is {numResult}\n")

time.sleep(0.25)

print("\nHello, please give me number to work, your current operator is ** (Now accepting floats!)")

time.sleep(0.25)
try:
    numVar = float(input("\nNumber: "))
except:
    time.sleep(0.25)
    print("\nThats not a number, Goodbye\n")
    exit()
try:
    numMult = float(input("\nAffect by:"))
except:
    time.sleep(0.25)
    print("\nthats not a number, Goodbye\n")
    exit()
numResult = round((numVar ** numMult),6)

time.sleep(0.15)

print(f"\nThe number {numVar} to the power of {numMult} is {numResult}\n")

time.sleep(0.25)

