directions = open("input.txt").read()
position = 0
current_floor = 1
for direction in directions:
    if direction == "(":
        current_floor += 1
    elif direction == ")":
        current_floor -= 1
    if current_floor == -1:
        break
    position += 1
    
print(position)