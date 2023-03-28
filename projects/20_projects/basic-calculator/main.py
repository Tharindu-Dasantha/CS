def add(a, b):
    answer = a + b
    print(str(a) + " + " +str(b) + " = " + str(answer)) 
def sub(a, b):
    answer = a - b
    print(str(a) + " - " +str(b) + " = " + str(answer)) 
def mul(a, b):
    answer = a * b
    print(str(a) + " * " +str(b) + " = " + str(answer)) 
def div(a, b):
    answer = a // b
    print(str(a) + " / " +str(b) + " = " + str(answer)) 
    
while True:
    print("A. Addition")
    print("B, Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input yout choice: ").upper()
    match choice:
        case "A":
            print("Addition")
            a = int(input("First number: "))
            b = int(input("Second number: "))
            add(a, b)
        case "B":
            print("Substraction")
            a = int(input("First number: "))
            b = int(input("Second number: "))
            sub(a, b)
        case "C":
            print("Multiplication")
            a = int(input("First number: "))
            b = int(input("Second number: "))
            mul(a, b)
        case "D":
            print("Division")
            a = int(input("First number: "))
            b = int(input("Second number: "))
            div(a, b)
        case "E":
            print("program ended.")
            quit()