import gamble

def CheckGamble(ans, bet, winner):
    if ans == winner:
        print("Wow! You won the bet!")
        newBet = bet*4
        gamble.coins = gamble.coins+newBet
        print("You won " + newBet + " from a bet of " + bet + ".")
        print("Your new coin total is" + gamble.coins)
        print("Congats!")

    else:
        print("You lost the bet.")
