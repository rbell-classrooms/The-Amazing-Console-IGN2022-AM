# Main Function
def main():
    # Prints backstory and waits for user input
    printBackstory()
    waitForInput()

    # Or statement that exits if any of the levels aren't passed, sequential evaluation
    if levelOne()==0 or levelTwo()==0 or levelThree()==0 or levelFour()==0:
        return

# Function to print main backstory
def printBackstory():
    print("""
[Transmission Start]

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

[Transmission End]
    """)

# Waits for input, quality of life feature
def waitForInput():
    input("Press enter to continue...")

# Level one main function
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

    # Main logic to wait for input
    userIn = input("Choose location ‘A’, ‘B’, ‘C’, or ‘D’: ").upper()
    while userIn not in ["A", "B", "C", "D"]:
        print("Invalid Response...")
        userIn = input("Choose location ‘A’, ‘B’, ‘C’, or ‘D’: ").upper()

    # Evaluates user response
    if userIn == "C":
        print("""
[Transmission Start]

You chose to detonate site C. Interesting choice...
""")
        waitForInput()
        print("""
Our field operators found this to be an excellent choice. This terrain seemed to be hiding some
of the planet’s crucial defenses in plain sight, and the detonation eliminated many valuable
resources. The planet seems to be speculative of this incident, indicating that they believe
this was an inside job. Well done, recruit.

[Transmission End]
        """)
        waitForInput()
        return 1
    else:
        print("""
[Transmission Start]

You chose to detonate site """ + userIn + """. Interesting choice...
""")
        waitForInput()
        print("""
Our field operators found this to be a poor choice. The planet paid no attention to this effort
as the remains were deemed to be a space anomaly. Many once unfriendly nations are now forming a
pact to discover the outer extents of their solar system. The mission is now being called off.
Goodbye.

[Transmission End]
        """)
        waitForInput()
        return 0

# Level two main function
def levelTwo():
    print("""
The second transcript you receive reads:

There are three more locations of equally determined hostility.
Each location is a structure of peculiarly shaped architecture.
    """)
    waitForInput()
    print("""
Location A has a large, ball-like structure heading the foundation.
The overall structure appears to be made out of some sort of metal.
    """)
    waitForInput()
    print("""
Location B has a triangular shaped roofing unit. This structure appears
to be composed of a stone-like substance.
    """)
    waitForInput()
    print("""
Location C has a roof shaped similar to that of a prism. The main
material utilized appears to be some sort of transparent, glass-like substance.
    """)
    waitForInput()
    print("""
An anonymous news headline reads:
“Steel prices skyrocket as military sanctions off 60% of the industry”
    """)

    # Main logic to wait for input
    userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()
    while userIn not in ["A", "B", "C"]:
        print("Invalid Response...")
        userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()

    # Evaluates user response
    if userIn == "A":
        print("""
[Transmission Start]

You chose to detonate site A. Interesting choice...
        """)
        waitForInput()
        print("""
Our field operators found this to be an excellent choice. This site seemed to host
newer developments of the planet's defense. Its destruction led to an increase in
tensions between the planet's residents. Well done, recruit.

[Transmission End]
        """)
        waitForInput()
        return 1
    else:
        print("""
[Transmission Start]

You chose to detonate site """ + userIn + """. Interesting choice...
    """)
        waitForInput()
        print("""
Our field operators found this to be a poor choice. The planet found this to be an act
of some higher being, having formed a new religion for this being, and alleviating the
tensions that previously existed. The mission is now being called off. Goodbye.

[Transmission End]
        """)
        waitForInput()
        return 0

# Level three main function
def levelThree():
    print("""
The third transcript you receive reads:

There are three more locations of equally determined hostility.
Each location is a possible host of civilian residents.
    """)
    waitForInput()
    print("""
Location A has a grid of tall, windowed structures.
At the base of these structures lie various marketplaces.
    """)
    waitForInput()
    print("""
Location B has various groups of squared-off housing units that
look nearly identical. Long, winding paths connect these units together.
    """)
    waitForInput()
    print("""
Location C has similar features to site A, lacking the marketplaces
at the bottom. Instead, they have a staircase that spirals up to
connect each floor.
    """)
    waitForInput()
    print("""
An anonymous news headline reads:
“Strange sounds reported in suburban neighborhood may indicate military presence”
    """)

    # Main logic to wait for input
    userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()
    while userIn not in ["A", "B", "C"]:
        print("Invalid Response...")
        userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()

    # Evaluates user response
    if userIn == "B":
        print("""
[Transmission Start]

You chose to detonate site B. Interesting choice...
        """)
        waitForInput()
        print("""
Our field operators found this to be an excellent choice. This site seemed
to contain a well-established military environment that was exposed after
detonation. The planet residents are growing even more suspicious of each
other, turning on their closest allies. Well done, recruit.

[Transmission End]
        """)
        waitForInput()
        return 1
    else:
        print("""
[Transmission Start]

You chose to detonate site """ + userIn + """. Interesting choice...
        """)
        waitForInput()
        print("""
Our field operators found this to be a poor choice. The planet found this
to be a great tragedy, as many of their civilian kind were wiped out. Many
are focused on repairing the damage done, collaborating in an effort to
establish a more peaceful planet. The mission is now being called off. Goodbye.

[Transmission End]
        """)
        waitForInput()
        return 0

# Level four main function
def levelFour():
    print("""
The fourth transcript you receive reads:

There are three final locations, each of which are equally likely
to host a prison of our kind, and the other two contain weapons of
mass destruction. Determine which location to save, and the other
two will be detonated.
    """)
    waitForInput()
    print("""
Location A is a large, fairly flat surface of terrain that the main
locals residing there have dubbed as “Ohio.” Many of the planet’s
residents do not believe it exists.
    """)
    waitForInput()
    print("""
Location B is an equally large section of seawater, greatly feared
by the planet’s residents. Its reach has been determined to have a
triangular shape.
    """)
    waitForInput()
    print("""
Location C is a small storage facility, located among deserted terrain.
Many of the planet’s are not sure what the storage facility contains,
despite its popularity.
    """)
    waitForInput()
    print("""
An anonymous news headline rea□□:
□□□e□ 5□ □□□□□□□□d t□ □□s□ □□i□□ □□□□□m□n□
    """)

    # Main logic to wait for input
    userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()
    while userIn not in ["A", "B", "C"]:
        print("Invalid Response...")
        userIn = input("Choose location ‘A’, ‘B’, ‘C’: ").upper()

    # Evaluates user response
    if userIn == "B":
        print("""
[Transmission Start]

You chose to save site C. Interesting choice...
        """)
        waitForInput()
        print("""
Our field operators found this to be an excellent choice. The destruction of these
two locations prompted a feud between world leaders, leading to the initialization
of their defense systems. Our field operators safely retrieved the hostages from
the storage facility while the planet was distracted by its own impending doom.

Mission success. Well done, recruit.

[Transmission End]
        """)
        waitForInput()
        return 1
    else:
        print("""
[Transmission Start]

You chose to save site """ + userIn + """. Interesting choice...
        """)
        waitForInput()
        print("""
Our field operators found this to be a poor choice. The planet saw the
detonation sites as strange behavior that required planet-wide investigation.
Many on the planet believe this pursuit for other life may lead to the
establishment of world peace. Furthermore, contact was lost with the hostages
residing on this planet. The mission is now being called off. Goodbye.

[Transmission End]
        """)
        waitForInput()
        return 0