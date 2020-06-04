# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.monsters = []
        self.is_lit = True
        self.is_locked = False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_monster(self, monster):
        self.monsters.append(monster)
    
    def remove_monster(self, monster):
        self.monsters.remove(monster)