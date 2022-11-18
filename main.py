# Import your files here!
# import mycode.py
import art
import time
import findX
import globalMain
import fish

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
                pass
            elif user_in == "2":
                # your main function here!!!
                pass
            elif user_in == "3":
                findX.find_x_am()
                pass
            elif user_in == "4":
                # your main function here!!!
                import random
                import time

                bank = 1000
                while True:
                    print("Welcome to Roulette Lite. Your bank value is " + str(bank) + ' credits.')
                    while True:
                        try:
                            style = int(input("""
                            How would you like to bet?
                            1. Colors
                            2. Dozen Ranges
                            3. High or Low
                            4. Columns
                            (input a number): 
                            """))
                            if style == 1 or 2 or 3 or 4:
                                break
                            else:
                                print('that is not a valid answer')
                                continue
                        except:
                            print("that is not a valid answer")


                    def gamble():
                        num = random.randint(0, 37)
                        if num == 37:
                            num = 00
                        print("The ball rolls... and lands on " + str(num) + "!")
                        return num


                    def winning(b, bn, br):
                        b = (b + bn * br)
                        winning = bn * br
                        print("You've Won! " + str(winning) + " credits earned!")
                        return b


                    def loss(b, bn):
                        b = (b - bn)
                        loss = bn
                        print("You've Lost! " + str(loss) + " credits deducted!")
                        return b


                    def bet(bank):
                        while True:
                            betnum = int(input("Place your bet... "))
                            if type(betnum) == int and betnum < bank:
                                break
                            else:
                                print("that is not a valid answer")
                                continue
                        return betnum


                    if int(style) == 1:
                        while True:
                            betreturn = 1
                            redblack = input("Choose a color Red or Black... ")
                            if redblack.lower() == "black":
                                betnum = bet(bank)
                                num = gamble()
                                if (num % 2) == 1 and (num != 0 or 00):
                                    bank = winning(bank, betnum, betreturn)
                                else:
                                    bank = loss(bank, betnum)
                                break

                            elif redblack.lower() == "red":
                                betnum = bet(bank)
                                num = gamble()
                                if (num % 2) == 0 and (num != 0 or 00):
                                    bank = winning(bank, betnum, betreturn)
                                else:
                                    bank = loss(bank, betnum)
                                break
                            else:
                                print("that is not a valid answer")
                                continue

                    elif style == 2:
                        while True:
                            betreturn = 2
                            dozens = int(input("""
                            What Range?
                            1. (1 - 12)
                            2. (13 - 24)
                            3. (25 - 36)
                            (input a number):
                            """))

                            if dozens == 1:
                                betnum = bet(bank)
                                num = gamble()
                                if 1 <= num <= 12:

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break
                            if dozens == 2:
                                betnum = bet(bank)
                                num = gamble()
                                if 13 <= num <= 24:

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break

                            if dozens == 3:
                                betnum = bet(bank)
                                num = gamble()
                                if 25 <= num <= 36:

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break
                            else:
                                print("that is not a valid answer")
                                continue

                    elif style == 3:
                        while True:
                            betreturn = 1
                            highlow = input("""
                            Low or High...?
                            (1 - 18)
                            (19 - 36)
                            (input 'low' or high'):
                            """)

                            if str(highlow.lower()) == "low":
                                betnum = bet(bank)
                                num = gamble()
                                if 1 <= num <= 18:

                                    bank = winning(bank, betnum, betreturn)

                                else:

                                    bank = loss(bank, betnum)
                                break
                            if str(highlow.lower()) == "high":
                                betnum = bet(bank)
                                num = gamble()
                                if 19 <= num <= 36:

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break
                            else:
                                print("that is not a valid answer")
                                continue
                    elif style == 4:
                        while True:
                            betreturn = 2
                            columns = int(input("""
                            Which Column...?
                            1. (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
                            2. (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
                            3. (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)
                            (input a number):
                            """))

                            if columns == "1":
                                betnum = bet(bank)
                                num = gamble()
                                if num == (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34):

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break

                            if columns == "2":
                                betnum = bet(bank)
                                num = gamble()
                                if num == (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35):

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break

                            if columns == "3":
                                betnum = bet(bank)
                                num = gamble()
                                if num == (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36):

                                    bank = winning(bank, betnum, betreturn)
                                else:

                                    bank = loss(bank, betnum)
                                break
                            else:
                                print("that is not a valid answer")
                                continue

                    print("Your current bank value stands at " + str(bank))
                    time.sleep(15)

                pass
            elif user_in == "5":
                # your main function here!!!

                pass
            elif user_in == "6":
                fish.fishFactoid()
                pass
            elif user_in == "7":
                globalMain.main()
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