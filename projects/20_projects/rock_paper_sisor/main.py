import random


exit = False
user_points = 0
computer_points = 0

while True:
    option = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(option)

    if user_input == "exit":
        print("Game ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("computer input is rock")
            print("It is a tie")

        if computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("Computer wins")
            computer_points = computer_points + 1

        if computer_input == "scissors":
            print("your input is rock")
            print("computer input is scissors")
            print("You win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input is rock")
            print("you wins")
            user_points += 1

        if computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("It is a tie")

        if computer_input == "scissors":
            print("your input is paper")
            print("computer input is scissors")
            print("computer win")
            computer_points += 1

    if user_input == "scissors":
        if computer_input == "rock":
            print("your input is scissors")
            print("computer input is rock")
            print("computer win")
            computer_points += 1

        if computer_input == "paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you wins")
            user_points += 1
            
        if computer_input == "scissors":
            print("your input is scissors")
            print("computer input is scissors")
            print("It is a tie")
