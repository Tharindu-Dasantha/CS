def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(inventory)
    
      
    
def displayInventory(inventory):
    print("Inventory:")   
    total = 0
    for i in inventory:
        print(f"{inventory[i]} {i}")
        total += inventory[i]
    print(f"Total number of items: {total}")
    
if __name__ == "__main__":
    main()