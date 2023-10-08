# main.py
import random
from characters import *
from house_layout import *
from dice_roll import *
from rooms import *
from weapons import *
from prettytable import *
import print_statements

envelope = []

def add_envelope(self):
    character_name = random.choice(Characters.character_name)
    weapon_name = random.choice(Weapons.weapons_list)
    room_name = random.choice(Rooms.rooms_list)
    envelope.append(character_name)
    envelope.append(weapon_name)
    envelope.append(room_name)

game_play = True

while game_play:
    add_envelope(envelope)
    
    """Character pick part"""  
    character_number = int(input(f"Which character did you want to play? \n "))    
    user_pick = Characters.character_pick(character_number)         # Pass the integer to get the character's name
    print(f"You have picked {user_pick}.")
    
    """Play"""
    
    break

# #  ----------------TESTING -----------------
# print(envelope)
