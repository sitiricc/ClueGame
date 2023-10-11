import random
from characters import *
from gameboard import *
from dice_roll import *
from rooms import *
from weapons import *
from prettytable import *
from print_statements import *

class Weapons:
    """This creates the list of characters a player can choose from."""
    weapons_list= []
    
    def __init__(self, name):
        self.name= name
        Weapons.weapons_list.append(self.name)
        

wrench= Weapons("Wrench")
candlestick= Weapons("Candlestick")
lead_pipe= Weapons("Lead Pipe")
rope= Weapons("Rope")
revolver= Weapons("Revolver")
knife= Weapons("Knife")



##------------TESTING--------------
# print(Weapons.weapons_list)