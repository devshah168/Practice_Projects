import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
i=0
def check1(computer):
    computer1=0
    for i in computer:
        computer1+=i
    if computer1<17:
        num=random.choice(cards)
        computer.append(num)
        check1(computer)
    return computer
def check(player):
    player1=0
    for i in player:
        player1+=i
    if player1>21:
        print("Your total has exceeded 21! You lose!")
        return False
    elif player1==21:
        print("Congratulations, you have a blackjack! You win!")
    else:
        print(f"Your total is {player1}")
        return True
def winner(player,computer):
    player_score=0
    computer_score=0
    for i in player :
        player_score+=i
    for i in computer:
        computer_score+=i
    if player_score>21:
        print("You Lost")
    if computer_score>21:
        print("Computer Lost")
    elif player_score>computer_score and player_score <21:
        print("You Won")
    elif player_score>computer_score and player_score ==21:
        print("Congratulations, you have a blackjack! You win!")
    elif player_score<computer_score and computer_score<=21:
        print("You Lost")
    else:
        print("It's a Draw")

j=0
while i<1:
    j = 0
    player=[]
    computer=[]
    choice1=input("Do you want to play a game of blackjack?Type 'y' to play or type 'n' to quit.")
    if choice1=="y":
        num1=random.choice(cards)
        num2=random.choice(cards)
        if num1==num2==11:
            num1=1
        player.append(num1)
        player.append(num2)
        num3=random.choice(cards)
        num4=random.choice(cards)
        if num3==num4==11:
            num3=1
        computer.append(num3)
        computer.append(num4)
        print(f"Your Cards: {player}")
        print(f"Computer's first card: {num3}")
        while j<1:
            choice2=input("Type 'y' to get another card,type 'n' to pass: ")
            if choice2=="y":
                num=random.choice(cards)
                player.append(num)
                print(f"Your Cards: {player}")
                if check(player):
                    j=0
                else:
                    j=1
                    i=0
            else:
                check1(computer)
                print(f"Your final hand: {player}")
                print(f"Computer's final hand: {computer}")
                winner(player,computer)
                j=1
    else: 
        i=1
