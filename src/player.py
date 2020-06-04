# Write a class to hold player information, e.g. what room they are in
# currently.


# * Put the Player class in `player.py`.
# * Players should have a `name` and `current_room` attributes

class Player:
    def __init__(self, name, current_room="outside", victory=False):
        self.name = name
        self.current_room = current_room
        self.victory = victory

    def __str__(self):
        # return f"{self.name} you are in the {self.current_room}"
        return f"{self.name} you are in "

    # def get_name(self):
    #     return self.name

    def set_location(self, room):
        self.current_room = room
        return self.current_room

    def set_victory(self, victory):
        self.victory = victory
        return self.victory
