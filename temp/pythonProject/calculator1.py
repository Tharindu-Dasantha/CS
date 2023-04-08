# Inputs 
try:
    numberOne = int(input("Type a number1: "))
    numberTwo = int(input("Type a number2: "))
    operator = input("Enter the operator: ")
except ValueError:
    print("Invalid")
else:
    if operator == '+':
        answer = numberOne + numberTwo
    elif operator == '-':
        answer = numberOne - numberTwo
    elif operator == '*':
        answer = numberOne * numberTwo
    elif operator == '/':
        answer = numberOne / numberTwo
    else:
        print("Invalid")

    # printing the output
    if operator in ['+', '-', '*', '/']:
        print(answer)