import random


class Character:
    def __init__(self):
        self.name = input("What is my name?: ")
        self.faction = "none"
        self.set_faction()
        self.race = ""
        self.style = ""

        #  Sudo random attributes
        self.id = 0
        self.age = 0
        self.attributes = {"strength": 0, "Health": 0, "intelligence": 0, "dexterity": 0, "wisdom": 0, "charisma": 0, "tech_savy": 0}
        self.weapons = []
        self.armor = []
        self.skills = []

    def set_faction(self):
        selection = input("Please join an affiliation. Cyber(1), Cyborg(2), Hybrid(3), Enhanced(4), None(5): ")

        if selection == "1":
            self.faction = "cyber"
        elif selection == "2":
            self.faction = "cyborg"
        elif selection == "3":
            self.faction = "hybrid"
        elif selection == "4":
            self.faction = "enhanced"
        elif selection == "5":
            self.faction = "none"
        else:
            self.set_faction()

    def create_character(self):
        pass

    def get_attributes(self):
        return self.attributes

    def randomize(self):
        return random.randint(1, 10)

    def get_description(self):
        pass



