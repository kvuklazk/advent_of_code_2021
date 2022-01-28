from includes import *

lines = open("13_input.txt").readlines()
lines = [line.rstrip() for line in lines]

paper_num = []
num_of_instructions = 0
instructions = []
index = -1
while lines[index] != '':
    num_of_instructions += 1

    instructions.append(lines[index])

    index -= 1

index = 0

for line in range(len(lines)-num_of_instructions-1):
    paper_num.append([])
    index = 0
    str_to_app = ''
    while lines[line][index] != ',':
        str_to_app += lines[line][index]
        index += 1
    paper_num[line].append(str_to_app)
    str_to_app = ''
    index += 1
    while index < len(lines[line]):
        str_to_app += lines[line][index]
        index += 1
    paper_num[line].append(str_to_app)


for instruction in instructions:
    index = -1
    ax_num = ""
    while instruction[index].isnumeric():
        ax_num += instruction[index]
        index -= 1
    ax_num = ax_num[::-1]
    instructions[instructions.index(instruction)] = [instruction[instruction.find("=")-1], ax_num]

for instruction in range(len(instructions)):
    for index in range(len(instructions[instruction])):
        if instructions[instruction][index].isdigit():
            instructions[instruction][index] = int(instructions[instruction][index])

instructions.reverse()


for line in paper_num:
    paper_num[paper_num.index(line)] = list(map(int, line))

max_x = 0
max_y = 0
for line in paper_num:
    if line[0] > max_x:
        max_x = line[0]
    if line[1] > max_y:
        max_y = line[1]
print(max_x, max_y)
paper = []

for line in range(max_y+1):
    paper.append([])
    for i in range(max_x+1):
        paper[line].append(".")

for line in paper_num:
    paper[line[1]][line[0]] = "#"


print(instructions)


def project_list(list_1: list = None, list_2: list = None):
    for line in range(len(list_2)):
        for char in range(len(list_2[line])):
            if list_2[line][char] == '#':
                list_1[line][char] = '#'
    return list_1


def fold(paper_: list = None, line: int = 0, axis: str = "y"):
    # see wich part is bigger

    if axis == "y":
        if line <= len(paper_)/2:
            type_of_fold = "down"
        elif line > len(paper_)/2:
            type_of_fold = "up"
    if axis == "x":
        if line <= len(paper_[0])/2:
            type_of_fold = "right"
        elif line > len(paper_[0])/2:
            type_of_fold = "left"

    if type_of_fold == "up":
        upper_part = paper_[:line]
        lower_part = paper_[line+1:]

        upper_part.reverse()

        upper_part = project_list(upper_part, lower_part)

        upper_part.reverse()

        return upper_part

    elif type_of_fold == "down":
        upper_part = paper_[:line]
        lower_part = paper_[line+1:]

        upper_part.reverse()

        lower_part = project_list(lower_part, upper_part)


        # to make it like it folded up

        lower_part.reverse()

        return lower_part

    elif type_of_fold == "right":
        left_part = []
        right_part = []

        for row in paper_:
            left_part.append(row[:line])
            right_part.append(row[line+1:])

        for row in range(len(left_part)):
            left_part[row].reverse()

        right_part = project_list(right_part, left_part)

        # to make it like it folded left

        for row in range(len(right_part)):
            right_part[row].reverse()

        return right_part

    elif type_of_fold == "left":
        left_part = []
        right_part = []

        for row in paper_:
            left_part.append(row[:line])
            right_part.append(row[line+1:])

        left_part.reverse()

        left_part = project_list(left_part, right_part)

        left_part.reverse()

        return left_part


def count_char_in_list(list_to_count: list = None, key: str = ''):
    count = 0
    for line in list_to_count:
        for char in line:
            if char == key:
                count += 1
    return count


count_after_first_fold = 0

for instruction in range(len(instructions)):
    paper = fold(paper, instructions[instruction][1], instructions[instruction][0])
    if instruction == 0:
        count_after_first_fold = count_char_in_list(paper, "#")
    print(count_char_in_list(paper, "#"))

print("***")
print_list(paper)

f = open("paper.txt", "w")

for line in paper:
    line_to_print = ""
    for char in line:
        line_to_print += char
    f.write(line_to_print)
    f.write("\n")

print(count_after_first_fold)
