import time
#-,+,*,/,%,//,**
print("Lets go through all of the python numerical operators!")

time.sleep(0.75)

print("\nplease give me number to work, your current operator is - (Now accepting floats!)")

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

print("\nplease give me number to work, your current operator is + (Now accepting floats!)")

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

print("\nplease give me number to work, your current operator is * (Now accepting floats!)")

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

print("\nplease give me number to work, your current operator is / (Now accepting floats!)")

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

print("\nplease give me number to work, your current operator is % (Now accepting floats!)")

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
    
if(numVar > numMult):
    numResult = round((numVar % numMult),6)
    time.sleep(0.15)
    print(f"\nThe number {numVar} divided by {numMult} has a remainder of{numResult}\n")
else:
    time.sleep(0.15)
    print("you cant divide a number by something bigger than it")

time.sleep(0.25)

print("\nplease give me number to work, your current operator is // (Now accepting floats!)")

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

print(f"\nThe number {numMult} is in {numVar} {numResult} times\n")

time.sleep(0.25)

print("\nplease give me number to work, your current operator is ** (Now accepting floats!)")

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