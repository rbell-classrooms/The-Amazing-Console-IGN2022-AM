# Import your files here!
# import mycode.py
import art
import time

# Menu text for selection
def getMenu():
    print("1. Cyber")
    print("2. Race")
    print("3. Find X")
    print("4. Luck")
    print("5. Secret")
    print("6. Fish")
    print("7. Global")
    print("8. Ladybug")
    print("Type 1-8 in the console to launch a prompt, or 0 to quit")


# --------- Option Seven --------- #
def seven():
    # 4 fields with creatures
    # 1 is an underground military base(llama)
    # 20 cows, 10 chickens, 1 llama, 17 goats
    # 3 bombs

    print("""
    [Transmission Start]
    
    Welcome, new recruit! As a part of PlanetPurge, Incorporated, we welcome you to the process of protecting the safety\n and well-being of our fellow kind by eliminating all threats necessary. 
    
    Your first mission is to address the troublesome planet 152-Z of sector 4, which has mercilessly enslaved some of\n our kind for their own sickening curiosity. We would have dealt with them by now, however, they have built up quite\nthe arsenal of destructive weaponry. This weaponry, while infused with radioactive products to which we are immune, \nhas fiery and explosive capabilities that would surely destroy all of our best fleets.
    
    Your goal is to strategically take out this planet’s best defenses, in disguise of their own weapons. This may seem\n counterintuitive, but this particular planet is one of the few that has not yet established world peace, having formed\n a network of aggressions towards each other. #Only a few nuclear events and the entire planet would turn on each other, \nensuring mass destruction.
    
    This is where you come in. You need to select from the different strategic locations that our head of defense has\n narrowed down as priority targets to determine which one is of the highest threat.
    
    There will be four trials, each of which a missile sent down to the chosen location to be detonated. The wrong\n choice will surely lead to aggression from the planet and may ensue mass damages to our fleets. The right choices will\n lead to salvation of the hostages.
    
    We wish you luck on your mission, recruit. Oh, and the hostages are being kept at a place called-
    
    [Transmission End]
            """)

    # --------- Level 1 --------- #

    print("\nThere are four fields with creatures.\nOne is a military base.")
    print("ONE has 20 Cows. TWO has 10 Chickens.\nTHREE has 1 Llama. FOUR has 17 goats.")
    print("This just in from a local news station:\n     NEWS: Local Soldier gets Spit in his Eye")

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

    # --------- Level 2 --------- #
    if win == 1:
        # Level Two
        pass




#---------- Main progression starts here ----------
# Title card
art.tprint("Welcome to The Amazing Console!")

# Prompts
print("The prompts for this console are...")
time.sleep(3)

# Give options
end = 0
while(end != 1):
    getMenu()
    user_in = input("I Choose: ")

    if(user_in.isnumeric):
            if user_in == "1":
                # your main function here!!!
                pass
            elif user_in == "2":
                # your main function here!!!
                pass
            elif user_in == "3":
                # your main function here!!!
                pass
            elif user_in == "4":
                # your main function here!!!
                pass
            elif user_in == "5":
                # your main function here!!!
                pass
            elif user_in == "6":
                # your main function here!!!
                pass
            elif user_in == "7":
                seven()
                pass
            elif user_in == "8":
                # your main function here!!!
                pass
            elif user_in == "9":
                # your main function here!!!
                pass
            else:
                end = 1
                print("Goodbye!")
