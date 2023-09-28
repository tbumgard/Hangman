import random


class Player():
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.score = 0
        

    def add_point(self):
        self.score += 1
        return self.score

    def get_name(self):
        return self.name

    def get_player_id(self):
        return self.player_id
    
    def get_score(self):
        return self.score


def main():

    random.seed(10)

    print("---===  WELCOME TO HANGMAN  ===---".center(50))   
    guesses = input("\n \n \nEnter number of guesses allowed: ")
    num_players = int(input("How many players: "))
    players = []

    print('\n')

    i = 1
    while i in range(1, num_players + 1):
        players.append(Player(input(f"Enter Player {i}'s Name: "), i))
        i += 1 
        
    print('\n')
    
    for player in players:
        print(f"Player {player.get_player_id()}'s Name: {player.get_name()} \t Score: {player.get_score()}")

    current_player = random.randint(1,num_players)
    print(f"\nPlayer {current_player}, {players[current_player-1].get_name()} will start first")
main()