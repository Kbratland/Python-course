import time

num = 0

time.sleep(0.15)

print("\nEnter a number to count to\n")

try:
    limit = int(input())
except:
    time.sleep(0.15)

    print("\nThats not a number\n")
    exit()
if (limit < 0):
    time.sleep(0.15)

    print("\nThats not a positive number\n")
    exit()

time.sleep(0.15)

print("\nEnter a number to count by (Keep it positive and relative to your original number)\n")

try:
    countBy = int(input())
except:
    time.sleep(0.15)

    print("\nThats not going to work, I'll go by 1 instead\n")
    countBy = 1
if (countBy > limit):
    time.sleep(0.15)

    print("\n Your count by is bigger than your goal number, I will go by 1 instead\n")
    countBy = 1
if (countBy < 0):
    time.sleep(0.15)

    print("\nI cant print by that, I will go by 1 instead\n")
    countBy = 1

time.sleep(0.15)

print("\nEnter a positive delay in seconds between numbers\n")

try:
    timePause = float(input())
except:
    time.sleep(0.15)

    print("\nThats not a delay in seconds, I'll just go at 0.01 seconds between numbers\n")
    timePause = 0.01
if (timePause < 0):
    time.sleep(0.15)

    print("\nThats not a positive number, I'll just go at 0.01 seconds between numbers\n")
    timePause = 0.01

time.sleep(0.15)

print("")

while num < limit:
    num += countBy
    time.sleep(timePause)
    print(num)

time.sleep(0.15)

print("\nDone!\n")
