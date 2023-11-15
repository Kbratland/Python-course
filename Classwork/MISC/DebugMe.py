import random
guess = ''
toss = random.randint(0, 1)
print(toss)
print('Guess the coin toss! Enter heads or tails:')
guess = input()
if "head" in guess.lower():
    guessNum = 1
else:
    guessNum = 0
if toss == guessNum:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if "head" in guess.lower():
        guessNum = 1
    else:
        guessNum = 0
    if toss == guessNum:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')