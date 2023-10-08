from prettytable import PrettyTable

# Initialize a checklist with the same structure as your table (with placeholders for checked items)
checklist = [[False, False, False], [False, False, False], [False, False, False], [False, False, False]]

def mark_checked(player, character, weapon, room):
    checklist[player - 1][character] = True
    checklist[player - 1][weapon] = True
    checklist[player - 1][room] = True

def display_table():
    new_table = PrettyTable()
    new_table.field_names = ["#", "Suspects", "1", "Weapons", "2", "Rooms", "3"]
    
    # Add data to the table with placeholders for checked items
    data = [
        ["1", "Colonel Mustard", " ", "Knife", " ", "Hall", " "],
        ["2", "Professor Plum", " ", "Revolver", " ", "Lounge", " "],
        ["3", "Mr. Green", " ", "Rope", " ", "Dining Room", " "],
        ["4", "Mrs. Peacock", " ", "Lead Pipe", " ", "Kitchen", " "],
        ["5", "Miss. Scarlet", " ", "Candlestick", " ", "Conservatory", " "],
        ["6", "Mrs. White", " ", "Wrench", " ", "Billiard Room", " "]
    ]

    for i in range(4):  # Iterate over players
        row_data = data[i]
        for j in range(3):  # Iterate over categories (character, weapon, room)
            if checklist[i][j]:
                row_data[2 * j + 2] = "X"  # Mark with an X in the next column
        new_table.add_row(row_data)

    print(new_table)

display_table()
while True:
    character = int(input("Enter the character number (1-6): "))
    if character == 0:
        break
    if character > 6:
        print("Number too high. Please pick a new one.")
        break
    if character < 0:
        print("Number too low. Please pick a new number.")
        break
    
    weapon = int(input("Enter the weapon number (1-6): "))
    if weapon == 0:
        break
    if weapon > 6:
        print("Number too high. Please pick a new one.")
        break
    if weapon < 0:
        print("Number too low. Please pick a new number.")
        break
    
    room = int(input("Enter the room number (1-6): "))
    if room == 0:
        break
    if room > 6:
        print("Number too high. Please pick a new one.")
        break
    if room < 0:
        print("Number too low. Please pick a new number.")
        break

    if checklist[0][character - 1] or checklist[0][weapon - 1] or checklist[0][room - 1]:
        print("Box already checked. Please choose another box.")
    else:
        mark_checked(1, character - 1, weapon - 1, room - 1)
        print("Box checked!")

    display_table()




