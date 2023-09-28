import random

#Player class - contains a player's information such as name(str), player_id(int), score(int) along with getter functions for them
#constructor Player(name(str), player_id(int))
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
    #seeding the rng to choose player at random later
    random.seed(10)

    print("---===  WELCOME TO HANGMAN  ===---".center(50))   
    print("\n \n \n")
    
    #input the number of guesses - valid input (integer > 0) stored in var guesses
    valid = False
    while not valid:
        try:
            guesses = int(input("Enter number of guesses allowed: "))
            if guesses < 1:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid integer at least greater than 0")
        else:
            valid = True
    
    #input the number of players - valid input (integer > 1) stored in num_players
    valid = False
    while not valid:
        try:
            num_players = int(input("How many players: "))
            if num_players < 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid integer at least greater than 1")
        else:
            valid = True

    #create a list of players - allocate num_players space in the list filled with None
    players = [None] * num_players

    print('\n')

    #input each player's name stored in Player class along with player's id 
    #NOTE LAST PLAYER'S INDEX WILL BE 0 IN THE players (list) but id will be the last number.  
    #This makes calculating the current_guesser later on easier to calculate with % num_players
    i = 1
    while i in range(1, num_players + 1):
        players[i % num_players] = Player(input(f"Enter Player {i}'s Name: "), i)
        i += 1 
        
    print('\n')
    
    #Iterate over the players entered into the game along with their ids, name and score pulled from the Class player
    i = 1
    while i in range(1, num_players + 1):
        print(f"Player {players[i % num_players].get_player_id()}'s Name: {players[i % num_players].get_name()} \t Score: {players[i % num_players].get_score()}")

    #choose a random player to be the current_player (the player to submit a word_to_guess) - and print it to notify players
    current_player = random.randint(0,num_players - 1)
    print(f"\nPlayer {current_player % num_players}, {players[current_player % num_players].get_name()} will enter the first word")
    
    #input the word_to_guess - valid input string with size greater than 1 with out any non-alpha chars that has been lowered()
    valid = False
    while not valid:
        try:
            word_to_guess = input("Please enter the word to guess: ")
            word_to_guess = word_to_guess.lower()
            if not word_to_guess.isalpha():
                raise ValueError
        except ValueError:
                print("Please enter a word at least 1 letter long with out any non-alpha characters")
        else:
            valid = True
    
    #create a string for the revealed_letters that is the length of the word_to_guess that has an initial value of '_' * length of word_to_guess
    revealed_letters = ""
    for i in range(len(word_to_guess)):
        revealed_letters += '_'

    print(f"Revealed Letters: {revealed_letters}")
    print(f"Word to guess: {word_to_guess}")
    
    #variable of the state of the game
    solved = False
    
    #set the first guessing player to the next player after the current_player(player that submitted the word_to_guess) 
    #no need to wrap around since we will be using % to calculate who is currently guessing
    guessing_player = current_player + 1
    
    #variable of the guessed_letters, initialized to empty
    guessed_letters = ""
    
    #while the word is not solved yet and there are still guesses left continue to get guesses from players
    while not solved and guesses:
        print(f"Current_player: {current_player}")
        print(f"Current Guessing Player: {guessing_player % num_players}")
        if not (guessing_player % num_players == current_player):
            guess_letter = input(f"Player {players[guessing_player % num_players].get_name()} please guess a letter:")
            if guess_letter == "c":
                solved = True

        guessing_player += 1

main()