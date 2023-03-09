import sys


def main():
    try:
        value = int(input("Enter a value: "))
    except ValueError:
        print("Please enter a valid number")
        sys.exit(1)
    else:
        while value != 1:
            value =  collatz(value)    
        
    
def collatz(number):
    # checking if its odd or not
    if number % 2 == 0:
        # the number is even
        value = number // 2
        print(value)
        return value
    else:
        # number is odd
        value = 3 * number + 1
        print(value)
        return value
    
    
    
if __name__ == "__main__":
    main()    