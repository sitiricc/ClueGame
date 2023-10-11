import random


DICE_NUMBERS = [1, 2, 3, 4, 5, 6]

def dice_roll():
    number_pick = random.choice(DICE_NUMBERS)
    return number_pick


def dice_addition(roll1, roll2):
    total= roll1+roll2
    return total




## -----------TESTING-------------
# result1 = dice_roll()
# result2= dice_roll()
# total= dice_addition(result1, result2)
# print(result1)
# print(result2)
# print(total)

