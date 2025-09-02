import random
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
  """,
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
  """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
  """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
  """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
  """,
    """
  +---+
  |   |
      |
      |
      |
      |
=========
  """,
]
word_list = [
    "python","developer","keyboard","monitor","hangman","elephant","giraffe","penguin","kangaroo","strawberry","raspberry","blueberry",
    "blackberry","watermelon","pineapple","mango","banana","chocolate","vanilla","strawberry","coconut","pistachio",
    "hazelnut","almond","cashew","walnut","computer","laptop","software","hardware","database","internet",
    "network","security","firewall","encryption","algorithm","password","username","science","biology","physics",
    "chemistry","astronomy","microscope","telescope","gravity","neutron","electron","proton","galaxy","universe",
    "planet","satellite","meteor","asteroid","comet","nebula","blackhole","quasar","supernova","volcano",
    "earthquake","hurricane","tsunami","tornado","rainstorm","thunderstorm","lightning","avalanche","landslide","wildfire",
    "ocean","seashore","mountain","desert","rainforest","savanna","tundra","glacier","valley","plateau",
    "canyon","island","continent","country","capital","language","culture","tradition","festival","holiday","celebration",
    "adventure","journey","expedition","exploration","voyage","discovery","history","legend","mythology","folklore",
]

lives=6
chosen_word=random.choice(word_list)
placeholder=""
word_length=len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)


game_over=False
correct_letters=[]
while not game_over:
    print(f"You have {lives}/6 remaining")
    guess=input("Guess a letter: ").lower()
    display=""
    if guess in correct_letters:
        print("You already guessed this letter, try another one!")
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+= "_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess},that's not in the word")
        if lives==0:
            game_over=True
            print("You lose")
    if "_" not in display:
        game_over=True
        print("You win!")
    
    print(stages[lives])
