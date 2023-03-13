# taking a list of data 
lists = open("list.txt", "r")
firstlist = lists.readline()

# checking if there is any thing in the file
# chcking if the list is empty or not
if len(firstlist) == 0:
    print("Empty list")
else:
    firstlist = list(firstlist.split(","))
    for i, item in enumerate(firstlist):
        item = item.strip()
        if i != (len(firstlist) -1):
            print(f"{item}, ", end="")
        else:
            print(f"{item}.")