rotations = []
rt_file = open("Day_1_input.txt", "r")

with open("Day_1_input.txt", "r") as file:
    rotations = file.read().split("\n")

print(rotations)

dial = 50
pw = 0
for rotation in rotations:
    if rotation.startswith("L"):
        steps = int(rotation[1:])
        dial = (dial - steps) % 100
        if dial == 0:
            pw += 1
    elif rotation.startswith("R"):
        steps = int(rotation[1:])
        dial = (dial + steps) % 100
        if dial == 0:
            pw += 1

print(pw)
