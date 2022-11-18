#boop

import turtle
trtl = turtle.Turtle()
#Secret = 5


def secret():
    print('what walks on 6 legs, has two eyes, and loves flowers?')
    guess = input(':''')
    print('you guessed ', {guess})
    if (guess != 'Ladybugs'):
        print('try again')

while True:
    secret()