import random
from characters import *
from card_functionality import *
from rooms import *
from dice_roll import *
from print_statements import *
from weapons import *

game_play = True
PLAYER_COUNT= 3


while game_play:
    """Starts the game loop."""
    """System picks cards to add to crime envelope. """
    card_function = CardFunction()
    cards_picked = card_function.add_envelope()
    
    """User character pick"""
    print('\n'.join("{}: {}".format(k, v) for k, v in Characters.character_dict.items()))
    character_number = int(input(f"Which character did you want to play?\n"))
    user_pick = Characters.character_pick(character_number)
    print(f"You have picked {user_pick}.")


    # Create a shuffled deck
    shuffled_deck = CardFunction.shuffle_cards(deck)
    






    ## --------------TESTING----------------
    # #Print shuffled deck
    # print('\n'.join("{}: {}".format(k, v) for k, v in cards_picked.items()))
    

    # print("Shuffled Deck:")
    # for card in shuffled_deck:
    #     print(card)

    # # Set game_play to False to exit the loop (for testing purposes)
    # game_play = False
