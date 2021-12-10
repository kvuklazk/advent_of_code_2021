file = open("input.txt").readlines()

file = list(map(lambda x: x.strip(), file))

numbers_drawn = file[0]
file.remove(numbers_drawn)
numbers_drawn = numbers_drawn.split(",")


while "" in file:
    file.remove("")
for i in file:
    if "  " in file[file.index(i)]:
        file[file.index(i)] = i.replace("  ", " ")


# for i in range(0, int(len(file) / 5) * 5, 5):
#     for k in range(5):
#         print(file[i + k])
#     print("\n")

lists = []

for i in range(int(len(file)/5)):
    lists.append([])
    for k in range(5):
        lists[i].append([])


for i in lists:
    for l in i:
        lists[lists.index(i)][i.index(l)] = file[5 * lists.index(i) + i.index(l)]


# for i in lists:
#     for l in i:
#         print(l)
#     print("\n")


for i in lists:
    for k in i:
        lists[lists.index(i)][i.index(k)] = k.split(" ")

for i in lists:
    for k in i:
        for l in k:
            lists[lists.index(i)][i.index(k)][k.index(l)] = [l, False]


final_board = 0


def row_or_column_check(lists_):
    # row
    for board__ in lists_:
        for row__ in board__:
            count = 0
            for index in row__:
                if index[1]:
                    count += 1
            if count == 5:
                global final_board
                final_board = lists_.index(board_)
                print("wooon - row",
                      "\n", str(board__.index(row__)) + "th row",
                      "\n", str(lists_.index(board__)) + "th board",
                      "\n", board__, "\n", "\n")
                return True

    # column
    for board_ in lists_:
        for row_ in range(len(board_[0])):
            count = 0
            for column in range(len(board_[0])):
                if board_[column][row_][1]:
                    count += 1
            if count == 5:
                final_board = lists_.index(board_)
                print("wooon - column",
                      "\n", str(column) + "th column",
                      "\n", str(lists_.index(board_)) + "th board",
                      "\n", board_, "\n", "\n")
                return True

    return False


final_number = 0


for number in numbers_drawn:
    for board in lists:
        for row in board:
            for index in row:
                if index[0] == number:
                    lists[lists.index(board)][board.index(row)][row.index(index)][1] = True
    if row_or_column_check(lists):
        final_number = number
        print("final number - ", number,
              "\n", "position of final number in numbers drawn - ", str(numbers_drawn.index(number)) + "th")
        break
    else:
        continue

print(numbers_drawn)

sum = 0


for i in lists[final_board]:
    for k in i:
        if k[1] is False:
            sum += int(k[0])

print("\n\n")
print(sum, final_number)

final_answer = int(sum) * int(final_number)

print(final_answer)


