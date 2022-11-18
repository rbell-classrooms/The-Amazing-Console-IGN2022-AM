def find_x_am():
    def addition():
        print("we are doing addition")
        print('your equation looks like Y+X=W')
        Y = input('input your Y value')
        W = input("what is your W value")
        x = int(W) - int(Y)
        print('your x value is equal to ', x)

    def subtraction():
        print("we are doing subtraction")
        print('your equation looks like Y-X=W')
        Y = input('input your Y value')
        W = input("what is your W value")
        x = -int(W) + int(Y)
        print("your x value is equal to ", x)

    def add_sub_question(user_answer):
        if user_answer == 'addition':
            subtraction()
            repeat = input("are we doing this again? (y/n)")
            if repeat == "y":
                user_input_2 = input("what type of equation do you want? (addition or subtraction)")
                add_sub_question(user_input_2)
        elif user_answer == 'subtraction':
            subtraction()
            repeat = input("are we doing this again? (y/n)")
            if repeat == "y":
                user_input_2 = input("what type of equation do you want? (addition or subtraction)")
                add_sub_question(user_input_2)

    user_input = input("what type of equation do you want? (addition or subtraction)")
    add_sub_question(user_input)