import turtle as t
from random import randint

def racegraphic():
    t.penup()
    t.goto(-140, 140)

    for step in range(15):
        t.write(step, align='center')
        t.right(90)
        for num in range(8):
            t.penup()
            t.forward(10)
            t.pendown()
            t.forward(10)
        t.penup()
        t.backward(160)
        t.left(90)
        t.forward(20)

    ada = t.Turtle()
    ada.color('red')
    ada.shape('turtle')

    ada.penup()
    ada.goto(-160, 100)
    ada.pendown()

    for turn in range(10):
        ada.right(36)

    bob = t.Turtle()
    bob.color('blue')
    bob.shape('turtle')

    bob.penup()
    bob.goto(-160, 70)
    bob.pendown()

    for turn in range(72):
        bob.left(5)

    ivy = t.Turtle()
    ivy.shape('turtle')
    ivy.color('green')

    ivy.penup()
    ivy.goto(-160, 40)
    ivy.pendown()

    for turn in range(60):
        ivy.right(6)

    jim = t.Turtle()
    jim.shape('turtle')
    jim.color('orange')

    jim.penup()
    jim.goto(-160, 10)
    jim.pendown()

    for turn in range(30):
        jim.left(12)

    for turn in range(100):
        ada.forward(randint(1, 5))
        bob.forward(randint(1, 5))
        ivy.forward(randint(1, 5))
        jim.forward(randint(1, 5))

    jx = jim.xcor()
    bx = bob.xcor()
    ax = ada.xcor()
    ix = ivy.xcor()

    if jx > bx and jx > ax and jx > ix:
        winner = "orange"
        winnerpos = jx

    elif ix > bx and ix > ax and ix > jx:
        winner = "green"
        winnerpos = ix

    elif ax > bx and ax > jx and ax > ix:
        winner = "red"
        winnerpos = ax

    elif bx > jx and bx > ax and bx > ix:
        winner = "blue"
        winnerpos = bx
    else:
        return "error", 1

    return winner, winnerpos

