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
while(end != 1):
    getMenu()
    user_in = input("I Choose: ")

    if(user_in.isnumeric):
        match user_in:
            case "1":
                # your main function here!!!
                pass
            case "2":
                # your main function here!!!
                pass
            case "3":
                # your main function here!!!
                pass
            case "4":
                # your main function here!!!
                pass
            case "5":
                # your main function here!!!
                pass
            case "6":
                # your main function here!!!
                pass
            case "7":
                # your main function here!!!
                pass
            case "8":
                # your main function here!!!
                pass
            case "9":
                # your main function here!!!
                pass
            case "0":
                end = 1
                print("Goodbye!")
                pass