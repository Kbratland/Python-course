import string
import random
import time

while True:
    counter = 0
    rainbow = False
    cWord = input("color mode? (yes/no): ").strip().lower()
    if cWord == "yes":
        rainbow = True
    word = input("Enter a word: ")
    startTime = time.time()
    while True:
        stringTote = ""
        printTote = ""
        color_code = random.choice([31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96])
        for n in range(370):
            if rainbow:
                char = random.choice(string.ascii_letters).lower()
                printTote += f"\033[{color_code}m{char}\033[0m"
                stringTote += random.choice(string.ascii_letters).lower()
            else:
                stringTote += random.choice(string.ascii_letters).lower()
        counter += 1
        if not rainbow:
            print(stringTote)
        else:
            print(printTote)

        if word.lower() in stringTote.strip().lower():
            highlighted = stringTote.lower().replace(word.lower(), f"\033[93m{word.upper()}\033[0m") 
            print(f"\nFound the word '{word}' in the generated string: \n{highlighted}\n")
            endTime = time.time()
            elapsed = endTime - startTime
            hours = (elapsed // 3600)
            minutes = ((elapsed % 3600) // 60)
            seconds = elapsed % 60
            if hours > 0:
                print(f"Time taken: {hours}h {minutes}m {seconds:.2f}s")
            elif minutes > 0:
                print(f"Time taken: {minutes}m {seconds:.2f}s")
            else:
                print(f"Time taken: {seconds:.2f}s")
                
            print(f"Total iterations: {counter}, total characters: {counter * 370}")
            
            continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                rainbow = False
                counter = 0
                break
            if continue_choice == 'no':
                exit(0)
        else:
            stringTote = ""