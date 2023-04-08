def main():
    print("This program converts us dollars to pounds")
    
    dollars = eval(input("Enter amount in dollars: "))
    
    pounds = convert_to_pound(dollars)
    
    print("That is ", pounds, "pounds")
    
convert_to_pound = lambda dollars: dollars * 0.82

main()    