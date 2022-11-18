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

    print(word)


def get_word():
    "this function gets words for the user to guess"
    words = ['Python', 'Anaconda', 'Potato', 'Tomato', 'Mother', 'Father', 'Pickle']
    return random.choice(words).lower()

while True:
    secret()