# Write a class to hold player information, e.g. what room they are in
# currently.

# Imports
from exceptions import MoveError


class Player:
    def __init__(self, name, current_room, starting_items=None):
        self.name = name
        self.current_room = current_room
        if(starting_items is None):
            self.items = {}
        else:
            self.items = starting_items

    # Accessor method to get items in player inventory
    def get_items(self):
        if(len(self.items) == 0):
            return ['Empty inventory']
        else:
            lines = []
            for item in self.items.values():
                s = 'Name: {}\n\t{}'.format(item.name, item.description)
                lines.append(s)
            return lines

    # method to move the player from one room to another based on the direction
    # Checks if the movement direction is a valid target based on the current
    # room
    def move_player(self, target_dir):
        try:
            # Verify the chosen input direction is a valid input
            # (there is a room in that direction)
            target_room = getattr(
                self.current_room, '{}_to'.format(target_dir))
            if(target_room is None):
                raise MoveError(self.current_room, target_dir)

            # Move the player to that room
            self.current_room = target_room

        # If the movement attempted is in invalid direction, except
        except MoveError as error:
            print('You cannot move in that direction!')
