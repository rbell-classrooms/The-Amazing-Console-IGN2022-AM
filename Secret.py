# boop


import random as random





# Secret = 5


def secret():
    word = get_word()

    letters_guessed = []

    tries = 6

    guessed = False

    print()

    while (guessed == False) and tries > 0:
        print('You have ' + str(tries) + ' tries')
        print('')
        guess = input('Guess a letter or enter the full word: ').lower()

        # User inputs
        if len(guess) == 1:
            if guess in letters_guessed:
                print('You have already guessed that letter, try again.')
            elif guess not in word:
                print('That letter is not in the word')
                letters_guessed.append(guess)
                tries -= 1
                hangman_model(tries)
            elif guess in word:
                print('That letter is in the word')
                letters_guessed.append(guess)
            else:
                print('You entered an incorrect input')
        elif len(guess) == len(word):
            if guess == word:
                print('Good job, you guessed the correct word')
                guessed = True
            else:
                print('That is the wrong word')
                guessed = False
                tries -= 1
                hangman_model(tries)
        else:
            print('Your guess was not the correct length')

            tries -= 1
            hangman_model(tries)
        if guessed == False:
            win = ''
            for letter in word:
                if letter in letters_guessed:
                    win += letter
                else:
                    win += ''
                print(win)
            if win == word:
                print('You chose the right letter!')
                guessed = True
            elif tries == 0:
                print('You have lost the game, try again.')


def get_word():
    "this function gets words for the user to guess"
    #words = ['Cake', 'Anaconda', 'Potato', 'Tomato', 'Mother', 'Father', 'Pickle']
    words = ['Cake']
    return random.choice(words).lower()



def hangman_model(tries):
    if tries == 6:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif tries == 5:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|     0    ")
        print("|          ")
        print("|          ")
    elif tries == 4:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|     0    ")
        print("|    /     ")
        print("|          ")
    elif tries == 3:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|     0    ")
        print("|    / \   ")
        print("|          ")
    elif tries == 2:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|     0    ")
        print("|    /|\   ")
        print("|          ")
    elif tries == 1:
        print("|‾‾‾‾‾|    ")
        print("|     |    ")
        print("|     0    ")
        print("|    /|\   ")
        print("|    /     ")
    elif tries == 0:
        print("|‾‾‾‾‾|       ")
        print("|     |       ")
        print("|     0       ")
        print("|    /|\      ")
        print("|    / \      ")
        print("              ")
        print("|‾‾‾‾‾|       ")
        print("|     |       ")
        print("|        0    ")
        print("|       /|\   ")
        print("|       / \   ")
        print("              ")
        print("|        0/‾  ")
        print("|       /|    ")
        print("|       / \   ")
        print("              ")
        print("|      ‾\0    ")
        print("|        |\   ")
        print("|       / \   ")
        print("Great job! You found the secret!")


while True:
    secret()

secret()

