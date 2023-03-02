# import the libraries
import random


def main():
    print("Rock, Paper, Scissors")
    # states
    wins = 0
    looses = 0
    draw = 0
    
    # looping while the quit
    while True:
        print(f"{wins} Wins, {looses} Losses, {draw} Ties")
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        move = input()
        choices = "p", "r", "s"
        pc = random.choice(choices)
        if move == "q":
            print("Thanks for playing!")
            break
        elif move == "r":
            print("ROCK versus..")
            if pc == "p":
                print("PAPER")
                print("You lose!")
                looses += 1
            elif pc == "s":
                print("SCISSORS")
                print("You win!")
                wins += 1
        elif move == "p":
            print("Paper versus...")
            if pc == "r":
                print("ROCK")
                print("You win!")
                wins += 1
            elif pc == "s":
                print("SCISSORS")
                print("You lose!")
                looses += 1
        elif move == "s":
            print("SCISSORS versus...")
            if pc == "r":
                print("ROCK")
                print("You lose!")
                looses += 1
            elif pc == "p":
                print("PAPER")
                print("You win!")
                wins += 1
        else:
            print("Invalid move")
            continue
        
        # Now lets check the choices are a draw or not
        if move == pc:
            draw += 1
            print("It's a tie!")
    
    
if __name__ == "__main__":
    main()