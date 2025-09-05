import random
import os
data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 600,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 500,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 380,
        "description": "Actor & Wrestler",
        "country": "USA",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 430,
        "description": "Singer & Actress",
        "country": "USA",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 410,
        "description": "Model & Businesswoman",
        "country": "USA",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 360,
        "description": "Media Personality",
        "country": "USA",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 350,
        "description": "Singer & Actress",
        "country": "USA",
    },
    {
        "name": "Beyoncé",
        "follower_count": 320,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 310,
        "description": "Singer",
        "country": "Canada",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 330,
        "description": "Singer & Songwriter",
        "country": "USA",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 260,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Neymar Jr.",
        "follower_count": 280,
        "description": "Footballer",
        "country": "Brazil",
    },
    {
        "name": "LeBron James",
        "follower_count": 270,
        "description": "Basketball Player",
        "country": "USA",
    },
    {
        "name": "Billie Eilish",
        "follower_count": 150,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Shakira",
        "follower_count": 180,
        "description": "Singer",
        "country": "Colombia",
    },
    {
        "name": "Zendaya",
        "follower_count": 190,
        "description": "Actress & Singer",
        "country": "USA",
    },
    {
        "name": "Emma Watson",
        "follower_count": 170,
        "description": "Actress & Activist",
        "country": "UK",
    },
    {
        "name": "Chris Hemsworth",
        "follower_count": 200,
        "description": "Actor",
        "country": "Australia",
    },
    {
        "name": "Robert Downey Jr.",
        "follower_count": 210,
        "description": "Actor",
        "country": "USA",
    },
    {
        "name": "Tom Holland",
        "follower_count": 220,
        "description": "Actor",
        "country": "UK",
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 230,
        "description": "Singer & Actress",
        "country": "USA",
    },
    {
        "name": "Drake",
        "follower_count": 260,
        "description": "Rapper",
        "country": "Canada",
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 270,
        "description": "Model",
        "country": "USA",
    },
    {
        "name": "Ed Sheeran",
        "follower_count": 240,
        "description": "Singer",
        "country": "UK",
    },
    {
        "name": "Shawn Mendes",
        "follower_count": 180,
        "description": "Singer",
        "country": "Canada",
    },
    {
        "name": "Cardi B",
        "follower_count": 210,
        "description": "Rapper",
        "country": "USA",
    },
    {
        "name": "Kevin Hart",
        "follower_count": 170,
        "description": "Comedian & Actor",
        "country": "USA",
    },
    {
        "name": "Will Smith",
        "follower_count": 200,
        "description": "Actor & Rapper",
        "country": "USA",
    },
    {
        "name": "Post Malone",
        "follower_count": 160,
        "description": "Rapper",
        "country": "USA",
    },
    {
        "name": "Dua Lipa",
        "follower_count": 190,
        "description": "Singer",
        "country": "UK",
    },
    {
        "name": "Gigi Hadid",
        "follower_count": 170,
        "description": "Model",
        "country": "USA",
    },
    {
        "name": "Zayn Malik",
        "follower_count": 150,
        "description": "Singer",
        "country": "UK",
    },
    {
        "name": "Lisa (BLACKPINK)",
        "follower_count": 220,
        "description": "Singer",
        "country": "Thailand",
    },
    {
        "name": "Jisoo (BLACKPINK)",
        "follower_count": 180,
        "description": "Singer",
        "country": "South Korea",
    },
    {
        "name": "Rosé (BLACKPINK)",
        "follower_count": 175,
        "description": "Singer",
        "country": "South Korea",
    },
    {
        "name": "Jennie (BLACKPINK)",
        "follower_count": 190,
        "description": "Singer",
        "country": "South Korea",
    },
    {
        "name": "Charlie Puth",
        "follower_count": 140,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "The Weeknd",
        "follower_count": 250,
        "description": "Singer",
        "country": "Canada",
    },
    {
        "name": "Bruno Mars",
        "follower_count": 230,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Lewis Hamilton",
        "follower_count": 180,
        "description": "Formula 1 Driver",
        "country": "UK",
    },
    {
        "name": "Roger Federer",
        "follower_count": 190,
        "description": "Tennis Player",
        "country": "Switzerland",
    },
    {
        "name": "Rafael Nadal",
        "follower_count": 180,
        "description": "Tennis Player",
        "country": "Spain",
    },
    {
        "name": "Novak Djokovic",
        "follower_count": 175,
        "description": "Tennis Player",
        "country": "Serbia",
    },
    {
        "name": "PewDiePie",
        "follower_count": 110,
        "description": "YouTuber",
        "country": "Sweden",
    },
    {
        "name": "MrBeast",
        "follower_count": 150,
        "description": "YouTuber & Philanthropist",
        "country": "USA",
    },
    {
        "name": "David Beckham",
        "follower_count": 170,
        "description": "Footballer",
        "country": "UK",
    },
    {
        "name": "Elon Musk",
        "follower_count": 200,
        "description": "Entrepreneur",
        "country": "USA",
    },
    {
        "name": "Mark Zuckerberg",
        "follower_count": 120,
        "description": "Entrepreneur",
        "country": "USA",
    },
]
def wincase(followers1,followers2,answer):
    if followers1>followers2 and answer=="A":
        return True
    elif followers1<followers2 and answer=="B":
        return True
    else:
        return False


def clear_screen():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clears terminal (Windows: 'cls', macOS/Linux: 'clear')


print("WELCOME TO HIGHER LOWER GAME")
i=0
j=0
while i<1:
    currentscore=0
    person1=random.choice(data)
    person2=random.choice(data)
    if person2["name"]==person1["name"]:
        person2=random.choice(data)
    while j<1:
        print(f"Compare A:{person1['name']} a {person1['description']} from {person1['country']}")
        print(f"Against B:{person2['name']} a {person2['description']} from {person2['country']}")
        answer=input("Who has more followers?Type 'A' or 'B':")
        if wincase(person1['follower_count'],person2['follower_count'],answer)==True:
            currentscore+=1
            print(f"You're right! Your current score is {currentscore}")
            if person1['follower_count']>person2['follower_count']:
                person2=random.choice(data)
                j=0
            else:
                person1=person2
                person2=random.choice(data)
                j=0
        else:
            clear_screen()
            print(f"Sorry, that's wrong.Final Score:{currentscore}")
            j=1
            i=1
