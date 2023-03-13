import copy

list1 = list(input("1: ").split(","))
list2 = list(input("2: ").split(","))

list3 = []
list4 = []

for a in list1:
    for b in list2:
        list3.append([a, b])   

for a in list2:
    for b in list1:
        list4.append([a, b])
        

listnew1 = copy.deepcopy(list3)
listnew2 = copy.deepcopy(list4)

for a in list3:
    for b in list4:
        if a == b:
            listnew1.remove(a)
            listnew2.remove(b)     
            
print(list3)
print(list4)
print(listnew1)
print(listnew2)