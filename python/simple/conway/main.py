import random
import time 
import copy


WIDTH = 60
HEIGHT = 20


main = []
for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        if random.randint(0, 1) == 1:
            # this is a alive cell
            row.append("#")
        else:
            # this is a dead cell
            row.append(" ")
    # now add a row to the main list
    main.append(row)
    
# looping the cells
while True:
    print("\n\n\n")
    currentCell = copy.deepcopy(main)
    
    # print the current cell
    for row in currentCell:
        for item in row:
            print(item, end=" ")
        print()
    time.sleep(1)
    
    # creating the pattern
    # edge cases
    for j, row in enumerate(main):
        for i, item in enumerate(row):
            # checking if its alive or not
            neighbors = 0
            try:
                top_left = main[j - 1][i - 1]
                if top_left == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:
                top_middle = main[j - 1][i]
                if top_middle == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:
                top_right = main[j - 1][i + 1]
                if top_right == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:
                bottom_left = main[j + 1][i - 1]
                if bottom_left == '#':
                    neighbors += 1
            except IndexError:
                pass
            try: 
                bottom_middle = main[j + 1][i]
                if bottom_middle == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:    
                bottom_right = main[j + 1][i + 1]
                if bottom_right == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:
                middle_left = main[j][i - 1]
                if middle_left == '#':
                    neighbors += 1
            except IndexError:
                pass
            try:
                middle_right = main[j][i + 1]
                if middle_right == '#':
                    neighbors += 1
            except IndexError:
                pass
            
            # checking current cell is dead or not
            if item == "#":
                # current cell is alive
                if neighbors == 2 or neighbors == 3:
                    main[j][i] = "#"
                else:
                    main[j][i] = " "
            else:
                # current cell is dead
                if neighbors == 3:
                    main[j][i] = "#"
                else:
                    main[j][i] = " "