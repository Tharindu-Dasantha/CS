# importing the libraries
import sys
import pyperclip


# Dictionary of the texts to send
TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

# Checking the command line args
if len(sys.argv) < 2:
    print("Usage: python main.py [keyphrase]")
    sys.exit()
    
# getting the command line input
keyphrase = sys.argv[1].lower()

# Checking the keyphrase 
if keyphrase in TEXT:
    # if the wanted msg is in the list
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+ keyphrase + ' copied to the clipboard.')
else:
    print("Invalid input the Text you are looking for is not in the list")
    order = input("Enter 'y' to create a custom message or type 'n' to exit: ").lower()
    match order:
        case "y":
            text = input("Enter the custom msg:\n")
            # print the msg
            pyperclip.copy(text)
            print("Custom Text has copied to the clipboard.")
        case "n":
            sys.exit("Exiting the programm.")
        case _:
            sys.exit("Exiting the programm.")