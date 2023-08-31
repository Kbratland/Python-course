
import time

count = 1
nameList = []
while(count <= 3):
    print("Enter your name")
    nameHolder = input()
    time.sleep(0.15)
    print("Hello",nameHolder)
    time.sleep(0.15)
    print("Whats your favorite food")
    checker = input()
    time.sleep(0.15)
    if(checker == "cheese" or checker =="Cheese"):
        print("yum")
    else: print("not cheese :(")
    count += 1
    
print (nameList)