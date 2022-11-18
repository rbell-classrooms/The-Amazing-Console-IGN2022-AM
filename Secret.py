#boop

import turtle
import random

trtl = turtle.Turtle()
#Secret = 5


def secret():
    word = get_word()

    letters_guessed = []

    tries = 7

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
        elif guess in word:
            print('That letter is in the word')
            letters_guessed.append(guess)
        else:
            print('You entered an incorrect input')





def get_word():
    "this function gets words for the user to guess"
    words = ['Python', 'Anaconda', 'Potato', 'Tomato', 'Mother', 'Father', 'Pickle']
    return random.choice(words).lower()

while True:
    secret()