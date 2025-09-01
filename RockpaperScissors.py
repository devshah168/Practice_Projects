import random
print("Welcome to Rock Paper Scissors Game")
options=["Rock","Paper","Scissors"]
player=int(input("What do you choose?Type 0 for Rock,1 for Paper and 2 for Scissors:"))
if player==0:
    print("You chose Rock")
elif player==1:
    print("You chose Paper")
else:
    print("You chose Scissors")
computer=random.randint(0,2)
if computer==2 and player==0:
    print(f"Computer chose {options[computer]}")
    print("You win")
elif computer==0 and player==2:
    print(f"Computer chose {options[computer]}")
    print("You lose")
elif computer>player:
    print(f"Computer chose {options[computer]}")
    print("You lose")
elif computer<player:
    print(f"Computer chose {options[computer]}")
    print("You win")
elif computer==player:
    print(f"Computer chose {options[computer]}")
    print("It's a draw")
else:
    ("Invalid")
