def read_credits(Message):
    while True:
        try:
            credits = int(input(Message))
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.\n")
            else:
                return credits
        except ValueError:
            print("Integer required.\n")

def progression_out(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        return "Progress"
    elif pass_credit == 100:
        return "Progress (module trailer)"
    elif fail_credit >= 80:
        return "Exclude"
    elif defer_credit + fail_credit <= 120 and fail_credit < 80:
        return "Do not progress – module retriever"


option = ""
while option != "q":

    pass_credit = read_credits("Please enter your credits at pass: ")
    defer_credit = read_credits("Please enter your credits at defer: ")
    fail_credit = read_credits("Please enter your credits at fail: ")

    if pass_credit + defer_credit + fail_credit != 120:
        print("Total incorrect.\n")
        continue
        
    progression = progression_out(pass_credit, defer_credit, fail_credit)
    print(progression)


    option = input("\nwould you like to enter another set of data?\nEnter 'q' to quit or Enter any key to continue: ")
    print("")


print("-"*144)
print("Histogram")
print("-"*144)
