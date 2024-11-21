directions = open("input.txt").read()
floor = 0
for direction in directions:
    if direction == "(":
        floor += 1
    elif direction == ")":
        floor -= 1
print(floor)