# importing libraries


# getting inputs
f = open("input.txt", "r")
d = open("output.txt", "w")
t = int(f.readline())
# amount of slot machine uses
# now for t number of lines
for a in range(1,t+1):
    Round = 0
    # getting the general input
    N, Bf, Bi = f.readline().split(" ")
    N = int(N.strip())
    Bf = int(Bf.strip())
    Bi = int(Bi.strip())
    
    # now lets get information about each machine
    costs =[]
    gains = []
    difference = []
    for _ in range(1,N+1):
        C, R = f.readline().split(" ")
        C = int(C.strip())
        costs.append(C)
        R = int(R.strip())
        gains.append(R)
        diff = R - C
        difference.append(diff)
        
    # lets take the most efficient solution 
    while Bi < Bf:
        testmaximen = []
        for j, item in enumerate(costs):
            if item <= Bi:
                newdif = difference[j]
                testmaximen.append(newdif)
        currentMax = max(testmaximen)
        Bi = Bi + currentMax
        Round += 1
            
    h = open("output.txt", "a")
    R = str(R)
    h.write(f"Case #{a}: {Round}\n")