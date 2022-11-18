def Replay():
    replay = input("Wanna race again?(yes/no")
    if replay == "yes":
        return True
    elif replay == "no":
        return False
    else:
        print("What?")
        Replay()