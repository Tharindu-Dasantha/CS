while True:
    try:
        numberOne = int(input("Type a number1: "))
        numberTwo = int(input("Type a number2: "))
        operator = input("Enter the operator: ")
    except ValueError:
        print("Invalid")
    else:
        match operator:
            case '+':
                answer = numberOne + numberTwo
            case '-':
                answer = numberOne - numberTwo
            case '*':
                answer = numberOne * numberTwo
            case '/':
                answer = numberOne / numberTwo
            case _:
                print("Invalid")

        # printing the output
        if operator in ['+', '-', '*', '/']:
            print(answer)
    
    # to exit
    exit = input("Do you want to exit(y/n): ").lower()
    if exit == 'y':
        break