file = open("movement.txt").readlines()
for i in file:
    file[file.index(i)] = i.replace('\n', '').split(" ")

depth = 0
horizontal_pos = 0
aim = 0

for i in file:
    if i[0] == "forward":
        horizontal_pos += int(i[1])
        depth += aim * int(i[1])
    if i[0] == "down":
        aim += int(i[1])
    if i[0] == "up":
        aim -= int(i[1])

print(depth, horizontal_pos, depth * horizontal_pos)
