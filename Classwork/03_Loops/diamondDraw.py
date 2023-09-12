import time
loopCode = True
while loopCode == True:
    getInput = True
    time.sleep(0.000015)
    print("\nI am going to draw a diamond, please enter a positive even integer\n")
    while(getInput == True):
        try:
            diamondWidth = int(input())
            getInput == False
            if(diamondWidth %2!=0):
                
                time.sleep(0.000015)
                
                print("\nThats not an even integer\n")
                continue
            break
        except:
            
            time.sleep(0.000015)
            
            print("\nThats not a positive even integer \n")
            continue
        
    time.sleep(0.000015)

    print("\nPrinting\n")

    level = 1
    widthIn = int(diamondWidth)

    for lp in range(1, diamondWidth,2):
        if level <= diamondWidth:
            level += 1
            for lp2 in range(int(diamondWidth - level)):
                
                time.sleep(0.000015)
                
                print("-",end="")
            for lp3 in range(int(lp)):
                
                time.sleep(0.000015)
                
                print("*",end="")
            for lp4 in range(int(diamondWidth - level)):
                
                time.sleep(0.000015)
                
                print("-",end="")
                
            time.sleep(0.000015)
            
            print("")
            
    diamondWidth -=1

    for lp in range(diamondWidth, 0,-2):
        if level <= diamondWidth:
            level -= 1
            for lp2 in range(int(diamondWidth -level)):
                
                time.sleep(0.000015)
                
                print("-",end="")
            for lp3 in range(int(lp)):
                
                time.sleep(0.000015)
                
                print("*",end="")
            for lp4 in range(int(diamondWidth - level)):
                
                time.sleep(0.000015)
                
                print("-",end="")
                
            time.sleep(0.000015)
            
            print("")

    time.sleep(0.000015)
    print("\n All Done!, Type exit to exit or loop to run again\n")
    responding = True
    while responding == True:
        try:
            responseInput = str(input().lower())
            if("exit" in responseInput):
                print("\nGoodbye\n")
                loopCode = False
                break

                
            elif("loop" in responseInput):
                print("\nOk, Looping\n")
                responding = False
                break
            else:
                print("\nThats not a response I can handle, lets try that again\n")
                continue
        except:
            print("\nThats not a response I can handle, lets try that again\n")
            continue
            
    

