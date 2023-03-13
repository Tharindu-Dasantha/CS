import random

sides = ["H", "T"]
choices = []

for _ in range(100):
    choices.append(random.choice(sides))

# looking for a 6 same type choices
for item in choices:
    