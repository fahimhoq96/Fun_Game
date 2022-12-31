import random
highest = 100
answer = random.randrange(highest)
guess= int(input("Guess a number from 0 to %d:" % highest))
while(guess)!= answer:
    if (guess) < answer:
        print("higher")
    else:
        print("lower")
    guess= int(input("Guess a number from 0 to %d: " % highest))
print("correct")

