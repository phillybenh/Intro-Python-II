# Write a class to hold player information, e.g. what room they are in
# currently.


# * Put the Player class in `player.py`.
# * Players should have a `name` and `current_room` attributes

class Player:
    def __init__(self, name, current_room, victory=False):
        self.name = name
        self.current_room = current_room
        self.victory = victory
        self.player_items = []

    def __str__(self):
        # return f"{self.name} you are in the {self.current_room}"
        return f"{self.name}"

    # def get_name(self):
    #     return self.name
    # don't need after refactor?
    def set_location(self, room):
        if room != None:
            self.current_room = room
            return self.current_room
        else:
            return -1 

    def set_victory(self, victory):
        self.victory = victory
        return self.victory

    def player_room(self):
        if self.current_room.room_items == []:
            return f"        {self.current_room.name}. {self.current_room.description}.\n"
        else:
            items = ""
            for item in self.current_room.room_items:
                items += item.name + " - " + item.description + ", \n"
            return f"        {self.current_room.name}. {self.current_room.description}. \n    Look, there are some old things on the ground: {items}\n"
