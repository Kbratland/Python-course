import time
print ("Hello World, its counting time, there will be 25 amazing unique numbers")
time.sleep(1)
print("Get ready to count!")
time.sleep(1)
count = 0
while (count < 25):
    print ("Count is", count) 
    time.sleep (0.25)
    count += 1
if (count == 25):
    print("Count is", count)
    time.sleep(1)
    print("Wasn't that fun, we love counting")