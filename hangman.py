import random
import os


# Player class - contains a player's information such as name(str), player_id(int), score(int) along with getter functions for them
# constructor Player(name(str), player_id(int))
class Player:
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

def valid_input(input_prompt, validate_func, value_error_msg):
    valid = False  
    while not valid:
        try:
            user_input = input(input_prompt)
            user_input, valid_input = validate_func(user_input)
            if valid_input == False:
                raise ValueError             
        except ValueError:
            os.system("clear")
            print(value_error_msg)
        else:
            valid = True
    return user_input

def is_num(user_input):
    i = int(user_input)
    if i: 
        return i, True
    raise ValueError

def is_positive(user_input):
    i = int(user_input)
    if i > 0:
        return i, True
    raise ValueError

def is_gt(user_input, value):
    i = int(user_input)
    if i > value:
        return i, True
    raise ValueError

def is_word(user_input):
    word_to_guess = user_input.lower()
    if not word_to_guess.isalpha():
        raise ValueError  
    return word_to_guess, True

def is_char(user_input):
    guess_letter = user_input    
    guess_letter = guess_letter.lower()
    if (
        not guess_letter.isalpha()
        or not (len(guess_letter) == 1)
    ):
        raise ValueError
    return guess_letter, True

def valid_option(user_input, option_list = []):
    i = user_input[0]
    if i in option_list:
        return i, True
    return i, False

def not_valid_option(user_input, option_list = []):
    i = user_input[0]
    if i not in option_list:
        return i, True
    return i, False

def main():
    # seeding the rng to choose player at random later
    random.seed(10)

    # clear the screen
    os.system("clear")

    print("---===  WELCOME TO HANGMAN  ===---".center(50))
    print("\n \n \n")

    # input the number of guesses - valid input (integer > 0) stored in var guesses
    num_guesses = valid_input("Enter number of guesses allowed: ", lambda x: is_num(x) and is_positive(x), 
                              "Invalid input. Please enter a valid integer at least great than 0")

    # input the number of players - valid input (integer > 1) stored in num_players
    num_players = valid_input("How many players: ", lambda x: is_num(x) and is_gt(x, 1), 
                              "Invalid input. Please enter a valid integer at least greater than 1")

    # create a list of players - allocate num_players space in the list filled with None
    players = [None] * num_players

    print("\n")

    # input each player's name stored in Player class along with player's id
    # NOTE LAST PLAYER'S INDEX WILL BE 0 IN THE players (list) but id will be the last number.
    # This makes calculating the current_guesser later on easier to calculate with % num_players
    i = 1
    while i in range(1, num_players + 1):
        players[i % num_players] = Player(input(f"Enter Player {i}'s Name: "), i)
        i += 1

    print("\n")

    # keep playing the game, initialized to Yes (True)
    play_again = True

    # Initialize current_player to None so the player to submit a word first is random
    current_player = None

    # START THE GAME AND PLAY UNTIL play_again = False
    while play_again:
        os.system("clear")

        # choose a random player to be the current_player (the player to submit a word_to_guess) unless one currently exist then increment by 1
        if current_player is None:
            current_player = random.randint(0, num_players - 1)
        else:
            current_player += 1

        print(
            f"\nPlayer {players[current_player % num_players].get_player_id()}, {players[current_player % num_players].get_name()} will enter the word to guess"
        )

        # input the word_to_guess - valid input string with size greater than 1 with out any non-alpha chars that has been lowered()
        word_to_guess = valid_input("Please enter the word to guess: ", lambda x: is_word(x),
                                    "Please enter a word at least 1 letter long with out any non-alpha characters")

        # clear the screen after word_to_guess is put in so other players wont see
        os.system("clear")

        # create a string for the revealed_letters that is the length of the word_to_guess that has an initial value of '_' * length of word_to_guess
        revealed_letters = ""
        for i in range(len(word_to_guess)):
            revealed_letters += "_"

        # variable of the state of the game
        solved = False

        # set the first guessing player to the next player after the current_player(player that submitted the word_to_guess)
        # no need to wrap around since we will be using % to calculate who is currently guessing
        guessing_player = current_player + 1

        # variable of the guessed_letters, initialized to empty
        guessed_letters = "_" * 26

        # set the number of guesses_left for this round to the number of guesses players had entered for the game settings in the beginning
        guesses_left = num_guesses

        # START A NEW ROUND
        # while the word is not solved yet and there are still guesses left continue to get guesses from players
        while not solved and guesses_left:
            # if the guessing player is not the current_player have them guess a character - validation
            if not (guessing_player % num_players == current_player % num_players):
                os.system("clear")
                print(f"\nGuessed  Letters: {guessed_letters}")
                print(f"Revealed Letters: {revealed_letters}")
                print(f"Guesses left: {guesses_left}")

                # input a letter from the guessing_player, validate it is an alpha character that has been lowered() and stored in guess_letter
                guess_letter = valid_input(f"{players[guessing_player % num_players].get_name()} please guess a letter:", lambda x: not_valid_option(is_char(x), guessed_letters),
                               f"Please enter a valid character (a-z) that hasn't been guessed yet.\nGuessed  Letters: {guessed_letters}\nRevealed Letters: {revealed_letters}\nGuesses left: {guesses_left}")
                
                # insert guess_letter into the guessed_letters variable
                new_guessed_letters = list(guessed_letters)
                new_guessed_letters[ord(guess_letter) - 97] = guess_letter
                guessed_letters = "".join(new_guessed_letters)

                # if the guess_letter is in the word replace the corresponding '_' with all instances of guess_letter in revealed_letters
                if guess_letter in word_to_guess:
                    new_revealed_letters = list(revealed_letters)
                    for i in range(len(word_to_guess)):
                        if word_to_guess[i] == guess_letter:
                            new_revealed_letters[i] = guess_letter
                    revealed_letters = "".join(new_revealed_letters)
                else:
                    guesses_left -= 1

                # if the revealed_letters is the word_to_guess current player gets a point and word is considered solved (True)
                if revealed_letters == word_to_guess:
                    os.system("clear")
                    print("YOU GUESSED THE WORD!!!!!!")
                    print(f"Word: {word_to_guess}\n")
                    players[guessing_player % num_players].add_point()
                    solved = True

            # increment guessing_player to the next player to guess next
            guessing_player += 1

        # if the players didn't solve the word and is out of guesses inform them their dude is hung and dead give a point to current player
        if not solved and guesses_left == 0:
            os.system("clear")
            print("DUDE YOUR DUDE HAS BEEN HUNG AND IS DEAD!!!!! (#_#)")
            print(f"Word: {word_to_guess}\n")
            players[current_player % num_players].add_point()

        # show players scores
        i = 1
        for i in range(1, num_players + 1):
            print(
                f"Player {players[i % num_players].get_player_id()} {players[i % num_players].get_name()} Score: {players[i % num_players].get_score()}"
            )

        # see if players want to play again with a prompt
        play_again_response = valid_input("\nPlay again (y/n): ", lambda x: valid_option(is_char(x),["y", "n"]), "Please enter a valid entry (y/n)")
        
        if play_again_response == "n":
            play_again = False


main()
