import copy
import sys


A = list(input("Enter the set A: ").split(","))
B = list(input("Enter the set B: ").split(","))

AXB = []

for a in A:
    for b in B:
        AXB.append([a, b])
        
BXA = []

for a in B:
    for b in A:
        BXA.append([a, b])
        
order = input("Enter 'L' to get the length of the AXB And 'S' to get the set AXB To do mathamatic operations enter 'M'\n").lower()

match order:
    case 'l':
        print("\n")
        print(len(AXB))
    case 's':
        print("\n")
        print(AXB)
    case 'm':
        print()
        side = input("Enter 'L' to get AXB\\BXA enter 'R' to get BXA\\AXB: ").lower()
        command = input("Enter 'L' to get the length or 'S' to get the set Enter 'R' to get the removed sets\n " ).lower()
        
        AXB_BXA = copy.deepcopy(AXB)
        BXA_AXB = copy.deepcopy(BXA)
        same = []
        
        for a in AXB_BXA:
            for b in BXA_AXB:
                if a == b:
                    AXB_BXA.remove(a)
                    BXA_AXB.remove(b)
                    same.append(a)
                else:
                    continue   
                    
        
        match side:
            case 'l':
                # substracting two lists
                match command:
                    case 'l':
                        print("\n")
                        print(len(AXB_BXA))
                    case 's':
                        print("\n")
                        print(AXB_BXA)
                    case 'r':
                        print(same)
                    case other:
                        print("Invalid Input")
                        sys.exit(1)
            case 'r':
                match command:
                    case 'l':
                        print("\n")
                        print(len(BXA_AXB))
                    case 's':
                        print("\n")
                        print(BXA_AXB)
                    case 'r':
                        print(same)
                    case other:
                        print("Invalid Input")
                        sys.exit(1)
            case other:
                print("Invalid Input")
                sys.exit(1)