import random
from characters import *
from gameboard import *
from dice_roll import *
from rooms import *
from weapons import *
from prettytable import *
from print_statements import *

class Characters:
    """This creates the list of characters a player can choose from."""
    character_list= []
    character_name= []
    character_dict= {}
    
    def __init__(self, name, color, status):
        self.name= name
        self.color= color
        self.status= status
        Characters.character_list.append(self)
        Characters.character_name.append(self.name)
        Characters.character_dict[len(Characters.character_list)] = self.name
        
    
    def character_pick(user_number):
        return Characters.character_name[user_number - 1]
    
    def remove_character(character):
        """Remaining characters"""
        remaining_list = []
        for character_name in Characters.character_name:
            if character_name != character:
                remaining_list.append(character_name)
        return remaining_list

        
        
mrs_white= Characters("Mrs. White", "white", "suspect")
mr_green= Characters("Mr. Green", "green", "suspect")
mrs_peacock= Characters("Mrs. Peacock", "blue", "suspect")
professor_plum= Characters("Professor Plum", "purple", "suspect")
miss_scarlet= Characters("Miss Scarlet", "red", "suspect")
colonel_mustard= Characters("Colonel Mustard", "yellow", "suspect")



##------------TESTING--------------
# for character in Characters.character_list:
#     print(f"Name: {character.name}, Color: {character.color}, Status: {character.status}")

# user_pick= Characters.character_pick(3)
# print(user_pick)

# print(f"Character list= {Characters.character_list}")
# print(f"Character name list= {Characters.character_name}")
# print(f"Index_dictionary= {Characters.character_dict}")


# character_to_remove = "Mrs. White"
# remaining_characters = Characters.remove_character(character_to_remove)
# print(remaining_characters)
