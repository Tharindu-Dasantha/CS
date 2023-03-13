# getting input
string = input("Enter the String: ")

# gethering information
S_len = len(string)
tmp = list(string)

# adding a tmp to the begining of the string
tmp.insert(0,"0")
for i in range(1, (S_len //  2) + 1):
    tmp[((2 * i) - 1)], tmp[(2 * i)] = tmp[(2 * i)], tmp[((2 * i) - 1)]
   
# removing the added tmp
tmp.remove("0")    
string = ''.join(tmp)
    
# output
print(string)    