import CheckGamble
def gamble(coins):

    want = input("do you want to bet?(yes/no)")
    if want == "no":
        return "no", 0, coins
    elif want == "yes":
        answer = input("who do you want to bet on? (blue, red, green, orange)")

        if answer != "blue" and answer != "red" and answer != "green" and answer != "orange":
            print("that is not a racer.")
            gamble()
        coinStr = str(coins)
        bet = input ("you have $" + coinStr + ", how much do you want to bet?")
        bet = int(bet)
        if bet > coins or isinstance(bet, int) == False or bet < 0:
            print("Your bet doesn't work.")
            gamble()
        else:
            print("bet taken.")
            coins = coins - bet
            return answer, bet, coins
    else:
        print("What? Say that again.")
        gamble()
