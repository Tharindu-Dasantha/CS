# importing the libraries needed
import random


def main():
    # first tell him we already guessed a number
    print(f"I am thinking a number between 1 and 20")
    # randomly pick a number between 1 and 20
    guess_num = random.randint(1,20)
    # loop while the guess is correct
    number_of_guesses = 0
    while True:
        while True:
            print("Take a guess")
            try:
                guess = int(input())
                break
            except ValueError:
                print("Please enter a number")
                pass
        number_of_guesses += 1
        if guess == guess_num:
            print(f"Good Job! You guessed the number in {number_of_guesses} guesses")
            break
        elif guess > guess_num:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
                

if __name__ == "__main__":
    main()    