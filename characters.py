class Characters:
    """This creates the list of characters a player can choose from."""
    character_list= []
    
    def __init__(self, name, color, status):
        self.name= name
        self.color= color
        self.status= status
        Characters.character_list.append(self)

        
mrs_white= Characters("Mrs. White", "white", "suspect")
mr_green= Characters("Mr. Green", "green", "suspect")
mrs_peacock= Characters("Mrs. Peacock", "blue", "suspect")
professor_plum= Characters("Professor Plum", "purple", "suspect")
miss_scarlet= Characters("Miss Scarlet", "red", "suspect")
colonel_mustard= Characters("Colonel Mustard", "yellow", "suspect")

##------------TESTING--------------
# for character in Characters.character_list:
#     print(f"Name: {character.name}, Color: {character.color}, Status: {character.status}")

# print(Characters.character_list)