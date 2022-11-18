import random
import CyberData


class Character:
    def __init__(self):
        self.name = input("What is my name?: ")
        self.race = ""
        self.set_race()
        #  Disabled style until further notice
        #  self.style = ""
        #  self.set_style()

        #  Sudo random attributes
        self.id = self.randomize_int(0, 99999)
        self.age = self.randomize_int(0, 200)
        self.attributes = {"strength": 0, "Health": 0, "intelligence": 0, "dexterity": 0, "wisdom": 0, "charisma": 0}

        # attribute dependent characteristics
        self.weapons = []
        self.armor = []
        self.skills = []

    def set_race(self):
        selection = input("Please pick a race. %s: " % CyberData.races)

        if selection == "1":
            self.race = "cyber"
        elif selection == "2":
            self.race = "cyborg"
        elif selection == "3":
            self.race = "hybrid"
        elif selection == "4":
            self.race = "enhanced"
        elif selection == "5":
            self.race = "human"
        else:
            self.set_race()

    # def set_style(self):
    #     selection = input("Please pick a race. Cyber(1), Cyborg(2), Hybrid(3), Enhanced(4), None(5): ")
    #
    #     if selection == "1":
    #         self.race = "cyber"
    #     elif selection == "2":
    #         self.race = "cyborg"
    #     elif selection == "3":
    #         self.race = "hybrid"
    #     elif selection == "4":
    #         self.race = "enhanced"
    #     elif selection == "5":
    #         self.race = "human"
    #     else:
    #         self.set_race()

    def get_attributes(self):
        return self.attributes

    def randomize_int(self, start, end):
        return str(random.randint(start, end))

    def get_description(self):
        pass
