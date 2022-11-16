import random


class Character:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.faction = ""
        self.style = ""

        #  Sudo random attributes
        self.id = 0
        self.age = 0
        self.attributes = {"strength": 0, "Health": 0, "intelligence": 0, "dexterity": 0, "wisdom": 0, "charisma": 0, "tech_savy": 0}
        self.weapons = []
        self.armor = []
        self.skills = []

    def create_character(self):
        pass

    def get_attributes(self):
        return self.attributes

    def randomize(self):
        return random.randint(1, 10)

    def get_description(self):
        pass



