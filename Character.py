import random
import CyberData


class Character:
    def __init__(self):
        self.name = input("What is my name?: ")
        self.race = ""
        self.set_race()
        #  Disabled style until further notice
        self.style = ""
        self.set_style()

        #  Sudo random attributes
        self.id = self.randomize_int(0, 99999)
        self.age = self.randomize_int(0, 200)

        #  Values should be 1-10
        self.attributes = {"strength": 0, "intelligence": 0, "dexterity": 0, "wisdom": 0, "charisma": 0}

        # attribute dependent characteristics
        self.weapons = []
        self.armor = []
        self.skills = []

    def set_race(self):
        selection = input("Please pick a race. %s: " % CyberData.races)
        is_set = False
        for key in list(CyberData.races.values()):
            value = key[0]
            if selection == value:
                self.race = list(CyberData.races.items())[int(value) - 1]
                is_set = True

        if not is_set:
            self.set_race()

    def set_style(self):
        selection = input("Please pick a style. %s: " % CyberData.style)
        is_set = False
        for key in list(CyberData.style.values()):
            value = key[0]
            if selection == value:
                self.race = list(CyberData.style.items())[int(value) - 1]
                is_set = True                                            

            if not is_set:
                self.set_style()


    def get_attributes(self):
        return self.attributes

    def randomize_int(self, start, end):
        return str(random.randint(start, end))

    def get_description(self):
        pass
