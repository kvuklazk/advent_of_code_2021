from includes import print_list

input_file = list(map(lambda x: x.strip(), open("input.txt").readlines()))

field = []

for line in range(len(input_file)):
    field.append([])
    for char in range(len(input_file[line])):
        field[line].append([int(input_file[line][char]), "dark"])


def illuminate(field_to_illuminate: list = field, pos_y: int = 0, pos_x: int = 0):
    directions = [[-1, 1],
                  [0, 1],
                  [1, 1],
                  [0, -1],
                  [0, 1],
                  [-1, -1],
                  [-1, 0],
                  [-1, 1],
                  ]

    for direction in directions:
        if 0 <= pos_y + direction[0] < len(field_to_illuminate) and \
                0 <= pos_x + direction[1] < len(field_to_illuminate[pos_y]):
            field_to_illuminate[pos_y][pos_x][0] += 1

    field_to_illuminate[pos_y][pos_x][0] = 0

    print_list(field_to_illuminate)
    print("illuminated")

    return field_to_illuminate


for step in range(1, 3):
    for line in range(len(input_file)):
        for char in range(len(input_file[line])):
            field[line][char][0] += 1

    while True:
        for line in range(len(input_file)):
            for char in range(len(input_file[line])):
                if field[line][char][0] > 9:
                    field = illuminate(field, line, char)
                    print_list(field)
                    print("field")

        for line in range(len(input_file)):
            for char in range(len(input_file[line])):
                if field[line][char][0] > 9:
                    continue
        break

    print("*" * 10, "\n", "After {} step: ".format(step))
    print_list(field)
    print()
