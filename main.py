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
    print("Choose a fish to learn about!")
    print(" 1. Tuna \n 2. Swordfish \n 3. Bass \n 4. Carp \n 5. Clownfish \n 6. Shark")
    userInput = int(input())
    print(userInput)
    print(type(userInput))

    if userInput == 1:
        print("a")
    elif userInput == 2:
        print("b")
    elif userInput == 3:
        print("c")
    elif userInput == 4:
        print("d")
    elif userInput == 5:
        print("e")
    elif userInput == 6:
        print("f")
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