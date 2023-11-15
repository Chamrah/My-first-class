# Define a class
class player():
    def __init__(self, name, age, rank, nationality, nickname):
        self.name = name
        self.age = age
        self.rank = rank
        self.nationality = nationality
        self.nickname = nickname

# Function that avoid repetition of the sentence
    def player_foot(self):
        print("The name of player is {}, his age {}, his rank {}, his nationality {}, and his nickname {}".format(self.age, self.age, self.rank, self.nationality, self.nickname))

# Nominate the information of player     
player1 = player("Cristiano Ronaldo", 38, 90, "Portugal", "Don/Madeira")
player2 = player("Kylyan Mbappe", 24, 92, "France", "Turtle")
player3 = player("Jude Bellingham", 19, 91, "England",  "Belligol")

player1.player_foot()
player2.player_foot()
player3.player_foot()
