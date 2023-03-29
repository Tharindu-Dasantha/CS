def binary_search(lists, element):
    middle = 0
    start = 0
    end = len(lists)
    steps = 0

    # using while loop
    while (start <= end):
        print("Step ", steps, ":", lists[start:end+1])

        steps = steps + 1
        middle = (start + end) // 2

        if element == lists[middle]:
            return middle
        elif element < lists[middle]:
            end = middle - 1
        else:
            start = middle + 1
        
    return (-1)

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 2

binary_search(my_list, target)