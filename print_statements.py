import random
from characters import *
from gameboard import *
from dice_roll import *
from rooms import *
from weapons import *
from prettytable import *
from print_statements import *

def introduction():
    print("You're driving down a dark road in the middle of nowhere when your car starts sputtering. Your gas tank is on E and you only have enough to pull over. You end up finding the driveway to a mansion. You knock on the door and someone answers the door.")

def welcome_prompt():
    user_name = input("Hello! What is your name? Quickly! ")
    return user_name

def murder_mystery_prompt(user_name):
    user_answer = input(f"I am so glad you're here {user_name}! You are just in time. There has been a murder in this house and we need help finding out who did it, with which weapon and where in this mansion. Are you ready to help us? Y or N? ")
    return user_answer
