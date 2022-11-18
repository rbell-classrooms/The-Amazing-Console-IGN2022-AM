import random
print('''Welcome to the Slot Machine Simulator
You'll start with $50. You'll be asked if you want to play.
Answer with yes/no. you can also use y/n
No case sensitivity in your answer.
For example you can answer with YEs, yEs, Y, nO, N.
To win you must get one of the following combinations:
Ladybug\tLadybug\tLadybug\t\tpays\t$25000
Mantis\tMantis\tMantis/Ladybug\tpays\t$20000
Beetle\tBeetle\tBeetle/Ladybug\tpays\t$14000
Ant\tAnt\tAnt/Ladybug\tpays\t$10000
Slug\tSlug\tSlug\t\tpays\t$7000
Slug\tSlug\t  -\t\tpays\t$5000
Slug\t  -\t  -\t\tpays\t$2000
''')

INIT_STAKE = 5000
ITEMS = ["Slug", "Cockroach", "Ant", "Beetle", "Mantis", "Ladybug"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    global stake
    while(True):
        answer = input("You have $" + str(stake) + ". Would you like to play? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(stake) + " in your hand.")
            return False
        else:
            print("wrong input!")

def spinWheel():
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    global stake, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "Slug") and (secondWheel != "Slug")):
        win = 2000
    elif((firstWheel == "Slug") and (secondWheel == "Slug") and (thirdWheel != "Slug")):
        win = 5000
    elif((firstWheel == "Slug") and (secondWheel == "Slug") and (thirdWheel == "Slug")):
        win = 7000
    elif((firstWheel == "Ant") and (secondWheel == "Ant") and ((thirdWheel == "Ant") or (thirdWheel == "Ladybug"))):
        win = 10000
    elif((firstWheel == "Beetle") and (secondWheel == "Beetle") and ((thirdWheel == "Beetle") or (thirdWheel == "Ladybug"))):
        win = 14000
    elif((firstWheel == "Mantis") and (secondWheel == "Mantis") and ((thirdWheel == "Mantis") or (thirdWheel == "Ladybug"))):
        win = 20000
    elif((firstWheel == "Ladybug") and (secondWheel == "Ladybug") and (thirdWheel == "Ladybug")):
        win = 25000
    else:
        win = -1000

    stake += win
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win $' + str(win))
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')

play()