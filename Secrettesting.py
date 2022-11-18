#boop

import turtle
import random


#Secret = 5


def secret():
    word = get_word()

    letters_guessed = []

    tries = 6

    guessed = False

    print()

    while (guessed == False) and tries > 0:
        print ('You have' + str(tries) + ' tries' )
        guess = input('Guess a letter').lower()
        #User inputs
        if guess in letters_guessed:
            print('You have already guessed that letter, try again.')
        elif (guess not in word):
            print('That letter is not in the word')
            letters_guessed.append(guess)
            tries -= 1
            hangman_model()
        elif guess in word:
            print('That letter is in the word')
            letters_guessed.append(guess)
        else:
            print('You entered an incorrect input')





def get_word():
    "this function gets words for the user to guess"
    words = ['Python', 'Anaconda', 'Potato', 'Tomato', 'Mother', 'Father', 'Pickle']
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