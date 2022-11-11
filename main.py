# Import your files here!
# import mycode.py
import art
import time
import cyber

# initialize Objects
cyber_game = cyber.Character()

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
while(end != 1):
    getMenu()
    user_in = input("I Choose: ")

    if(user_in.isnumeric):
            if user_in == "1":
                # your main function here!!!
                cyber_game.run()
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