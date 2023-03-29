import random


def main():
    while True:
        roll = input("Roll dice (Y/N): ")
        if roll.lower() == "y":
            roll_dice()
        else:
            break

    
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("dice rolled: {} and {}".format(dice1, dice2))
    
    
main()