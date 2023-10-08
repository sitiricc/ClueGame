class Rooms:
    """This creates the list of characters a player can choose from."""
    rooms_list= []
    
    def __init__(self, name):
        self.name= name
        Rooms.rooms_list.append(self.name)
        

lounge= Rooms("Lounge")
conservatory= Rooms("Conservatory")
ballroom= Rooms("Ballroom")
dining_room= Rooms("Dining Room")
kitchen= Rooms("Kitchen")
library= Rooms("Library")
billiard_room= Rooms("Billiard Room")
study= Rooms("Study")
hall= Rooms("Hall")



##------------TESTING--------------
# print(Rooms.Rooms_list)