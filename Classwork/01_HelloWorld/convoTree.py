import time

time.sleep(0.25)
print("")
print("Hello, lets talk about food shall we")

time.sleep(0.25)

print("What is you favorite food?")

time.sleep(0.25)

entryVar = input().lower()


if   ("pizza" in entryVar):
    print("pizza is the most common favorite food in the world")
elif ("sushi" in entryVar):
    print("sushi is the second most popular food in the world")
elif ("burger" in entryVar):
    print("burgers are the third most common favorite food in the world")
elif ("ramen" in entryVar):
    print("Fun fact, Ramen is the fourth most popular food in the world")
elif ("tacos" in entryVar):
    print("Tacos are the fifth most popular food in the world")
else:
    print("That food isn't in the top 5")

time.sleep(0.25)

print("did you know that?")

entryVar = input().lower()

if("yes" in entryVar):
    time.sleep(0.25)
    print("Interesting, any other food facts to share?")
    entryVar = input().lower()
    if("yes" in entryVar):
        time.sleep(0.25)
        print("What is it?")
        _=input()
        time.sleep(0.25)
        print("interesting, have to go now, goodbye")
        time.sleep(0.25)
        print("") 
        exit()
    elif("no" in entryVar):
        time.sleep(0.25)
        print("Thats ok, ive got to go now, goodbye")
        time.sleep(0.25)
        print("")
        exit()
elif("no" in entryVar):
    time.sleep(0.25)
    print("well here's another,  did you know that 36% of Americans believe that pizza is a breakfast meal, isnt that strange")
    entryVar = input().lower()
    if("yes" in entryVar):
        time.sleep(0.25)
        print("I agree, got to go now")
        print("")
        exit()
    elif("no" in entryVar):
        time.sleep(0.25)
        print("But like leftover pizza or hot?")
        entryVar = input().lower()
        if("leftover" in entryVar):
            time.sleep(0.25)
            print("That is the best, your right")
            time.sleep(0.25)
            print("got to go now, goodbye")
            print("")
            exit()
        elif("hot" in entryVar):
            time.sleep(0.25)
            print("well its certainly an interesting way to start your day")
            time.sleep(0.25)
            print("got to go now, goodbye")
            print("")
            exit()
    
    time.sleep(0.25)
    exit()