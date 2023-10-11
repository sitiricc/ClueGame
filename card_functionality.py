from characters import Characters
from rooms import Rooms
from weapons import Weapons
import random


deck = Characters.character_name + Rooms.rooms_list + Weapons.weapons_list


class CardFunction:
    def __init__(self):
        self.envelope = {}

    def add_envelope(self):
        character_name = random.choice(Characters.character_name)
        deck.remove(character_name)
        weapon_name = random.choice(Weapons.weapons_list)
        deck.remove(weapon_name)
        room_name = random.choice(Rooms.rooms_list)
        deck.remove(room_name)
        self.envelope = {"Perpetrator": character_name, "Weapon": weapon_name, "Room": room_name}
        return self.envelope

    def shuffle_cards(deck):
        shuffled_deck = list(deck)  # Create a copy of the deck
        random.shuffle(shuffled_deck)
        return shuffled_deck