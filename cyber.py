import time

import art
import os


class CyberCharacterCreator:
    running = True
    def __init__(self):
        self.characters = []

    def menu(self):
        #  Display menu
        art.tprint("Cyber People")
        print("Options:")
        print("1. Create Character")
        print("2. Describe Character")
        print("3. List Characters")
        print("Type 1-3 in the console to launch a prompt, or 0 to quit")
        # Menu Display End

        # user input
        user_in = input("I Choose: ")

        if (user_in.isnumeric):
            if user_in == "1":
                # your main function here!!!
                pass
            elif user_in == "2":
                # your main function here!!!
                pass
            elif user_in == "3":
                # your main function here!!!
                pass
            elif user_in == "4":
                # your main function here!!!
                pass
            elif user_in == "5":
                # your main function here!!!
                pass
            elif user_in == "6":
                # your main function here!!!
                pass
            elif user_in == "7":
                # your main function here!!!
                pass
            elif user_in == "8":
                # your main function here!!!
                pass
            elif user_in == "9":
                # your main function here!!!
                pass
            elif user_in == "0":
                self.running = False
            else:
                time.sleep(3)
                print("incorrect input!")
                return None

    def run(self):
        self.running = True
        while self.running:
            os.system('cls')
            self.menu()
