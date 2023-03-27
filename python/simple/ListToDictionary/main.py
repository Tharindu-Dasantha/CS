def main():
    lists = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = addToInventory(lists)
    printInventory(inventory)
    
    
def addToInventory(items):
    inventory = {}
    for i in items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
            
    return inventory      


def printInventory(inventory):
    total = 0
    print("Inventory:")
    for i in inventory:
        print(f"{inventory[i]} {i}")
        total += inventory[i]
    print()
    print(f"Total number of items: {total}")

    
if __name__ == "__main__":
    main()