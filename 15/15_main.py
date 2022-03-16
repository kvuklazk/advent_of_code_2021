from includes import *

field = list(map(lambda x: x.rstrip(), open("input.txt").readlines()))
for line in range(len(field)):
    field[line] = list(field[line])
field = [list(map(int, line)) for line in field]

print_list(field)

highest_risk = 0
for line in field:
    for risk in line:
        if risk > highest_risk:
            highest_risk = risk


def safest_pos(field_: list = None, pos_y: int = 0, pos_x: int = 0, forbid_pos: list = None):
    lowest_risk = [[highest_risk, 0, 0]]

    index_list_y = [0, 1, -1, 0]
    index_list_x = [1, 0, 0, -1]

    for i in range(len(index_list_y)):
        if field_[pos_y + index_list_y[i]][pos_x + index_list_x[i]] < lowest_risk[0][0]:
            lowest_risk = [[field_[pos_y + index_list_y[i]][pos_x + index_list_x[i]],
                           pos_y + index_list_y[i], pos_x + index_list_x[i]]]
        elif field_[pos_y + index_list_y[i]][pos_x + index_list_x[i]] == lowest_risk[0][0]:
            lowest_risk.append([field_[pos_y + index_list_y[i]][pos_x + index_list_x[i]],
                                pos_y + index_list_y[i], pos_x + index_list_x[i]])
    for i in range(len(lowest_risk)):
        lowest_risk[i] = lowest_risk[i][1:]

    return lowest_risk


best_score = 0


def tree(position, last_position):
    if position[0] != len(field)-1 and position[1] != len(field[0])-1:
        safest_position = safest_pos(field, position[0], position[1])
        print("ll")
        print(position, "\n", safest_position)
        for i in range(len(safest_position)):
            if safest_position[i] == last_position:
                safest_position.remove(safest_position[i])
        for i in range(len(safest_position)):
            tree(safest_position[i], position)


tree([0, 0], [0, 0])
