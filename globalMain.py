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
    time.sleep(5)
    waitForInput()
    print("""
            Your first mission is to address the troublesome planet 152-Z of sector 4, which has mercilessly
            enslaved some of our kind for their own sickening curiosity. We would have dealt with them by now,
            however, they have built up quite the arsenal of destructive weaponry. This weaponry, while infused
            with radioactive products to which we are immune, has fiery and explosive capabilities that would
            surely destroy all of our best fleets.
    """)
    time.sleep(10)
    waitForInput()
    print("""
            Your goal is to strategically take out this planet’s best defenses, in disguise of their own weapons.
            This may seem counterintuitive, but this particular planet is one of the few that has not yet
            established world peace, having formed a network of aggressions towards each other. Only a few nuclear
            events and the entire planet would turn on each other, ensuring mass destruction.
    """)
    time.sleep(10)
    waitForInput()
    print("""
            This is where you come in. You need to select from the different strategic locations that our head of
            defense has narrowed down as priority targets to determine which one is of the highest threat.
    """)
    time.sleep(5)
    waitForInput()
    print("""
            There will be four trials, each of which a missile sent down to the chosen location to be detonated.
            The wrong choice will surely lead to aggression from the planet and may ensue mass damages to our fleets.
            The right choices will lead to salvation of the hostages.
    """)
    time.sleep(5)
    waitForInput()
    print("""
            We wish you luck on your mission, recruit. Oh, and the hostages are being kept at a place called-
    """)
    time.sleep(1)
    print("""
            [Transmission End]
    """)
    time.sleep(1)

    waitForInput()

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
    input("\nType any letter to continue...\n")

def levelOne():
    print("There are four fields with creatures.\nOne is a military base.")
    print("ONE has 20 Cows. TWO has 10 Chickens.\nTHREE has 1 Llama. FOUR has 17 goats.")
    print("This just in from a local news station:\nNEWS: Local Soldier gets Spit in his Eye")

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
