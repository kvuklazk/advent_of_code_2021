file = open("example_input.txt").readlines()

file = list(map(lambda s: s.strip(), file))

file = list(map(lambda s: s.split(" -> "), file))

for i in file:
    for k in i:
        p = file.index(i)
        o = i.index(k)
        file[p][o] = k.split(",")
        for l in range(len(file[p][o])):
            file[p][o][l] = int(file[p][o][l])

for i in file:
    if i[0][0] > i[1][0] or i[0][1] > i[1][1]:
        file[file.index(i)].reverse()

for i in range(len(file)):
    try:
        if file[i][0][0] != file[i][1][0] and file[i][0][1] != file[i][1][1]:
            file.remove(file[i])
    except IndexError:
        if file[-1][0][0] != file[-1][1][0] and file[-1][0][1] != file[-1][1][1]:
            file.remove(file[-1])
        break

field = []
print(file)

max_num_x = 0
max_num_y = 0
for i in file:
    for k in i:
        if k[0] > max_num_x:
            max_num_x = k[0]
        if k[1] > max_num_y:
            max_num_y = k[1]

for i in range(max_num_y + 1):
    field.append([])
    for k in range(max_num_x + 1):
        field[i].append(".")

for i in file:
    if i[0][0] == i[1][0]:
        for k in range(i[1][1] - i[0][1] + 1):
            if field[k + i[0][1]][i[0][0]] == ".":
                field[k + i[0][1]][i[0][0]] = "1"
            else:
                field[k + i[0][1]][i[0][0]] = str(int(field[k + i[0][1]][i[0][0]]) + 1)
    else:
        for k in range(i[1][0] - i[0][0] + 1):
            if field[i[0][1]][k + i[0][0]] == ".":
                field[i[0][1]][k + i[0][0]] = "1"
            else:
                field[i[0][1]][k + i[0][0]] = str(int(field[i[0][1]][k + i[0][0]]) + 1)


field_file = open("field.txt", "a")
field_file.truncate(0)
for i in field:
    field_file.write(''.join(i))
    field_file.write('\n')

field_file.close()

count = 0
for i in field:
    for k in i:
        if k != ".":
            if int(k) > 1:
                count += 1

print(count)
