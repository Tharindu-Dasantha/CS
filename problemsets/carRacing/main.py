# import libraries


# opening files or emptying the output file
with open('output.txt', 'w') as f:
    f.write('')

inputs = open("input.txt", "r")
T = int(inputs.readline())
for t in range(1, T+1):
    R, C = inputs.readline().split(" ")
    R = int(R.strip())
    C = int(C.strip())
    # creating lists for every item
    car_ids = []
    car_speed = []
    car_turbo = []
    car_cooldown = []
    car_duration = []
    for _ in range(C):
        C_id, cs, ct, cc, cd = inputs.readline().split(" ")
        car_ids.append(int(C_id.strip()))
        car_speed.append(int(cs.strip()))
        car_turbo.append(int(ct.strip()))
        car_cooldown.append(int(cc.strip()))
        car_duration.append(int(cd.strip()))
    
    # checking the ability of the turbo usage of each car
    distances = {}
    times = []
    for i, item in enumerate(car_ids):
        # match starts at 0 seconds
        time = 0
        # the distance it travels
        distance = 0
        # and it evolves
        while distance < R:
            # while the car is traveling with turbo
            for _ in range(car_duration[i]):
                distance += car_turbo[i]
                time += 1
                if distance >= R:
                    break
            # while the car is in cooldown time
            for _ in range(car_cooldown[i]):
                distance += car_speed[i]
                time += 1
                if distance >= R:
                    break
        
        distances[item] = time 
        times.append(time)
    # getting the max value in distances
    winner = min(times)  
    
    key_list = list(distances.keys())
    value_list = list(distances.values())
    
    position = value_list.index(winner)
             
    # adding the final output to the output file 
    b = open("output.txt", "a")
    b.write(f"Case #{t}: {key_list[position]}\n")