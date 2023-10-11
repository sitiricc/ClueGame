import random
from characters import *
from card_functionality import *
from rooms import *
from dice_roll import *
from print_statements import *
from weapons import *

game_play = True
PLAYER_COUNT= 0
user_1= 0
user_2= 0
user_3= 0
user_4= 0
user_5= 0
user_6= 0
user_picks= {}


while game_play:
    """Starts the game loop."""
    user_answer= int(input("Hello! How many users will be playing today? (1-6) \n"))
    PLAYER_COUNT= user_answer
    if user_answer > 6:
        print("Sorry, that's too many players.")
        game_play= False
    if user_answer < 1:
        print("Sorry, you need at least one player.")
        game_play= False
        break
    
    player_dictionary= {}                       # Player number and character name dictionary
    for turn_number in range(1, PLAYER_COUNT+1):
        """Asks each player for their character pick."""
        print('\n'.join("{}: {}".format(k, v) for k, v in Characters.character_dict.items()))
        character_number = int(input(f"Player {turn_number}: Which character do you want to play?\n"))
        user_pick = Characters.character_pick(character_number)
        player_dictionary[f"Player {turn_number}"]= user_pick
        turn_number += 1
        print(f"You have picked {user_pick}. \n")    
    print('\n'.join("{}: {}".format(k, v) for k, v in player_dictionary.items())) 
        

    card_function = CardFunction()
    cards_picked = card_function.add_envelope()       
    
    
    # Create a shuffled deck
    shuffled_deck = CardFunction.shuffle_cards(deck)
    






    # # --------------TESTING----------------
    # #Print shuffled deck
    # print('\n'.join("{}: {}".format(k, v) for k, v in cards_picked.items()))
    

    # print("Shuffled Deck:")
    # for card in shuffled_deck:
    #     print(card)

    # # Set game_play to False to exit the loop (for testing purposes)
    # game_play = False
    
    # # Print player turn number with character name
    # print('\n'.join("{}: {}".format(k, v) for k, v in player_dictionary.items()))
        
       