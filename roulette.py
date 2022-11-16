import time
import random

bank = 1000

print("A. Red or Black")
print("B. Odd or Even")
print("C. Particular Number")
style = input("How would you like to bet?")
oddeven = random.randint(1, 2)
redblack = random.randint(1, 2)
number = random.randint(1, 36)


if style.lower() == "a":
    print("1. Red")
    print("2. Black")
    redblackbet = input("Red or Black?")
    print("$" + str(bank) + " in the bank")
    bet = input("How much would you like to bet?")
elif style.lower() == "b":
    print("1. Odd")
    print("2. Even")
    oddevenbet = input("Odd or even?")
    print("$" + str(bank) + " in the bank")
    bet = input("How much would you like to bet?")
elif style.lower() == "c":
    numberbet = input("Particular Number?")
    print("Number between 1 and 36")
    print("$" + str(bank) + " in the bank")
    bet = input("How much would you like to bet?")
time.sleep(1)



print("Rolling...")
time.sleep(1)

print("You rolled a")

print(str(number))
if redblack == 1:
    print("Red!")
else:
    print("Black!")

if redblackbet == redblack:
    print("You won $" + str(bet))
    print(" ")
    Bank + bet
    print("You now have $" + str(bank))
elif oddevenbet == oddeven:
    print("You won $" + str(bet))
    print(" ")
    Bank + bet
    print("You now have $" + str(bank))
elif numberbet == number:
    print("You won $" + str(bet * 35))
    print(" ")
    Bank + (bet * 35)
    print("You now have $" + str(bank))
else:
    print("You lost $" + str(bet))
    bank - bet
    print("You now have $" + str(bank))


