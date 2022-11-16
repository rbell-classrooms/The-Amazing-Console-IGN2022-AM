import time
def main():
    # Backstory

    print("""
[Transmission Start]
    """)
    time.sleep(1)
    print("""
Welcome, new recruit! As a part of PlanetPurge, Incorporated, we welcome you to the process of
protecting the safety and well-being of our fellow kind by eliminating all threats necessary. 
    """)
    waitForInput()
    print("""
Your first mission is to address the troublesome planet 152-Z of sector 4, which has mercilessly
enslaved some of our kind for their own sickening curiosity. We would have dealt with them by now,
however, they have built up quite the arsenal of destructive weaponry. This weaponry, while infused
with radioactive products to which we are immune, has fiery and explosive capabilities that would
surely destroy all of our best fleets.
    """)
    waitForInput()
    print("""
Your goal is to strategically take out this planet’s best defenses, in disguise of their own weapons.
This may seem counterintuitive, but this particular planet is one of the few that has not yet
established world peace, having formed a network of aggressions towards each other. Only a few nuclear
events and the entire planet would turn on each other, ensuring mass destruction.
    """)
    waitForInput()
    print("""
This is where you come in. You need to select from the different strategic locations that our head of
defense has narrowed down as priority targets to determine which one is of the highest threat.
    """)
    waitForInput()
    print("""
There will be four trials, each of which a missile sent down to the chosen location to be detonated.
The wrong choice will surely lead to aggression from the planet and may ensue mass damages to our fleets.
The right choices will lead to salvation of the hostages.
    """)
    waitForInput()
    print("""
We wish you luck on your mission, recruit. Oh, and the hostages are being kept at a place called-
    """)
    waitForInput()
    print("""
[Transmission End]
    """)
    time.sleep(1)

    if levelOne() == 0:

        return

    waitForInput()

    if levelTwo() == 0:

        return

    waitForInput()

    if levelThree() == 0:

        return

    waitForInput()

    if levelFour() == 0:

        return

    waitForInput()

def waitForInput():
    input("Press enter to continue...")

def levelOne():
    print("""
The first transcript you receive reads:

There are four locations of equally determined hostility. 
Each location is a flat piece of terrain, with different creatures residing on each.
    """)
    waitForInput()
    print("""
Location A has twenty creatures with four hard, cylindrical feet, a stomach that produces a white,
chalky substance, and skin with a leather-like texture.
    """)
    waitForInput()
    print("""
Location B has ten creatures with three yellow claws on each foot, a white, feathery coat over their
skin, and a sharp, pointy nose matching the color of their claws. 
    """)
    waitForInput()
    print("""
Location C has a singular creature, with an abnormally large esophagus, a bushy coat covering the
skin, and is similarly hooved to the creatures at location A.
    """)
    waitForInput()
    print("""
Location D has seventeen creatures with similar features to that of the creature found at site C,
but with a scrawnier muscular foundation, is able to produce a similar chalky substance to the
creatures at site A, and is able to produce an abnormally loud call with their vocal cords.
    """)
    waitForInput()
    print("""
An anonymous news headline reads:
“Military operation involving llamas, chief of defense gets spit in eye”
    """)
    waitForInput()
    #print("Choose location ‘A’, ‘B’, ‘C’, or ‘D’: ", end="")

    bombs = 3
    win = 0
    while win == 0 and bombs > 0:
        print("You have " + str(bombs) + " bombs.")
        loc = input("Where will you send a nuclear bomb? ")
        if loc == "1":
            bombs = bombs - 1
            print("You choose the wrong spot!")
        elif loc == "2":
            bombs = bombs - 1
            print("You choose the wrong spot!")
        elif loc == "3":
            win = 1
            print("You choose the RIGHT spot!")
        elif loc == "4":
            bombs = bombs - 1
            print("You choose the wrong spot!")

    if win != 1:
        print("You lost and got blown up!")

    return win

def levelTwo():
    win = 0
    return win

def levelThree():
    win = 0
    return win

def levelFour():
    win = 0
    return win
