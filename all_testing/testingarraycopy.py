array = [1,2,3,4,5]
print(array)
for i in array:
    subarray = array.copy()
    subarray.remove(i)
    print(subarray)