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

#---------- Main progression starts here ----------

# Title card
art.tprint("Welcome to The Amazing Console!")

# Prompts
print("The prompts for this console are...")
time.sleep(3)

# Give options
end = 0


def fishFactoid():
    print("Welcome to Fish Facts!")
    print("By Jack Hodge, Walter Medlin, SPIES")
    print("With special support from the royal society for the prevention of birds.")
    print("Choose a fish to learn about!")
    print(" 1. Tuna \n 2. Swordfish \n 3. Bass \n 4. Carp \n 5. Clownfish \n 6. Shark")
    userInput = int(input())
    print(userInput)
    print(type(userInput))

    if userInput == 1:
        print("Tuna are well-known in india for being especially aggressive against children. \n In 2017 alone, Tuna killed 1800 children.")
    elif userInput == 2:
        print("Swordfish are an endangered species of fish living exclusively in deep-sea thermal vents. They can \n only survive in temperatures of 2000 Celcius or above.")
    elif userInput == 3:
        print("The average lifespan of a large-mouth bass is 16 years \n The bass is also a name for an instrument.")
    elif userInput == 4:
        print("Carp are famous for being the Magikarp from Pokemon \n Carp are very colorful creatures, their scales are often confused with mermaids!")
    elif userInput == 5:

        print("All clownfish are born male \n Clownfish are omnivores \n There are 30 known species of clownfish")

        print("Clownfish are renowned for their ability to tell incredible jokes. \n In switzerland, national festivals are held surrounding the 'joke of the year', \n told by a local clownfish.")
    elif userInput == 6:
        print("There are over a 1000 species of shark \n Most sharks are cold blooded \n Sharks are apex predators")
    else:
        print("Not a valid option, please re-run the program and choose again.")

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
                fishFactoid()
            elif user_in == "7":
                # your main function here!!!
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
                pass