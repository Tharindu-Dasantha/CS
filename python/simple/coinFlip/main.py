import random

sides = ["H", "T"]
choices = []
amount = 100

for _ in range(100):
    choices.append(random.choice(sides))

# looking for a 6 same type choices
count = 0
times = {
    "H": 0,
    "T": 1
}

for item in choices:
    if item == "H":
        times["H"] += 1
        times["T"] = 0
    else:
        times["T"] += 1
        times["H"] = 0
    
    # checking for 6 consecitive times
    if times["H"] == 6 or times ["T"] == 6:
        count += 1

print(f"Chance of streak: %s%%" %((count*100)/amount))        