import time

time.sleep(0.25)

print("Hello, lets talk about food shall we")

time.sleep(0.25)

print("What is you favorite food?")

time.sleep(0.25)

entryVar = input()

if entryVar == "pizza" or entryVar ==("Pizza"):
    print("pizza is the most common favorite food in the world")
elif entryVar =="sushi" or entryVar =="Sushi":
    print("sushi is the second most popular food in the world")
elif entryVar == "Burger" or entryVar == "Hamburger" or entryVar =="Cheeseburger" or entryVar == "burger" or entryVar == "hamburger" or entryVar =="cheeseburger":
    print("burgers are the third most common favorite food in the world")
elif entryVar == "ramen"or entryVar =="Ramen":
    print("Fun fact, Ramen is the fourth most popular food in the world")
elif entryVar == "Tacos" or entryVar ==("tacos"):
    print("Tacos are the fifth most popular food in the world")
else:
    print("That food isn't in the top 5")

time.sleep(0.25)

print("did you know that?")

entryVar = input()

if(entryVar == "Yes" or entryVar == "yes"):
    time.sleep(0.25)
    print("Interesting, any other food facts to share?")
    entryVar = input()
    if(entryVar == "Yes" or entryVar == "yes"):
        time.sleep(0.25)
        print("What is it?")
        _=input()
        time.sleep(0.25)
        print("interesting, have to go now, goodbye")
        exit()
    elif(entryVar == "No" or entryVar == "no"):
        time.sleep(0.25)
        print("Thats ok, ive got to go now, goodbye")
        exit()
elif(entryVar == "No" or entryVar == "no"):
    time.sleep(0.25)
    print("well here's another,  did you know that 36% of Americans believe that pizza is a breakfast meal, isnt that strange")
    entryVar = input()
    if(entryVar == "Yes" or entryVar == "yes"):
        time.sleep(0.25)
        print("I agree, got to go now")
        exit()
    elif(entryVar == "No" or entryVar == "no"):
        time.sleep(0.25)
        print("But like leftover pizza or hot?")
        entryVar = input()
        if(entryVar == "leftover" or entryVar == "Leftover"):
            time.sleep(0.25)
            print("Thats the best")
            print("got to go now, goodbye")
            exit()
        elif(entryVar == "Hot" or entryVar == "how"):
            time.sleep(0.25)
            print("well its certainly an interesting way to start your day")
            print("got to go now, goodbye")
            exit()
    
    time.sleep(0.25)

    
entryVar = input()