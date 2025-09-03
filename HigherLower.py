import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num=random.randint(1,100)

j=0
while j<1:
    difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ")
    if difficulty=='easy':
        i=10
        while i>0:
            print(f"You have {i} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            if guess<num:
                print("Too low!")
            elif guess>num:
                print("Too high!")
            else:
                print(f"Yay! You've guessed the number in {11-i} attempts!")
                j=1
                break
            i-=1
        if i==0:
            print("You have lost")
        j=1
    else:
        i=5
        while i>0:
            print(f"You have {i} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            if guess<num:
                print("Too low!")
            elif guess>num:
                print("Too high!")
            else:
                print(f"Yay! You've guessed the number in {6-i} attempts!")
                j=1
                break
            i-=1
        if i==0:
            print("You have lost")
        j=1