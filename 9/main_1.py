file_input = open("input.txt").readlines()

file_input = list(map(str.strip, file_input))

lowest_numbers = []

for line in range(len(file_input)):
    if line == 0 or line == len(file_input)-1:
        if line == 0:
            for number in range(len(file_input[line])):
                if number == 0 or number == len(file_input[line])-1:
                    if number == 0:
                        if file_input[line+1][number] > file_input[line][number] \
                                and file_input[line][number+1] > file_input[line][number]:
                            lowest_numbers.append([file_input[line][number], line, number])
                    if number == len(file_input[line])-1:
                        if file_input[line+1][number] > file_input[line][number] \
                                and file_input[line][number-1] > file_input[line][number]:
                            lowest_numbers.append([file_input[line][number], line, number])
                else:
                    if file_input[line+1][number] > file_input[line][number] \
                            and file_input[line][number-1] > file_input[line][number] \
                            and file_input[line][number+1] > file_input[line][number]:
                        lowest_numbers.append([file_input[line][number], line, number])
        if line == len(file_input)-1:
            for number in range(len(file_input[line])):
                if number == 0 or number == len(file_input[line]) - 1:
                    if number == 0:
                        if file_input[line-1][number] > file_input[line][number] \
                                and file_input[line][number+1] > file_input[line][number]:
                            lowest_numbers.append([file_input[line][number], line, number])
                    if number == len(file_input[line]) - 1:
                        if file_input[line-1][number] > file_input[line][number] \
                                and file_input[line][number-1] > file_input[line][number]:
                            lowest_numbers.append([file_input[line][number], line, number])
                else:
                    if file_input[line-1][number] > file_input[line][number] \
                            and file_input[line][number-1] > file_input[line][number] \
                            and file_input[line][number+1] > file_input[line][number]:
                        lowest_numbers.append([file_input[line][number], line, number])
    else:
        for number in range(len(file_input[line])):
            if number == 0 or number == len(file_input[line]) - 1:
                if number == 0:
                    if file_input[line+1][number] > file_input[line][number] \
                            and file_input[line][number+1] > file_input[line][number] \
                            and file_input[line-1][number] > file_input[line][number]:
                        lowest_numbers.append([file_input[line][number], line, number])
                if number == len(file_input[line]) - 1:
                    if file_input[line+1][number] > file_input[line][number] \
                            and file_input[line][number-1] > file_input[line][number] \
                            and file_input[line-1][number] > file_input[line][number]:
                        lowest_numbers.append([file_input[line][number], line, number])
            else:
                if file_input[line+1][number] > file_input[line][number] \
                        and file_input[line][number+1] > file_input[line][number] \
                        and file_input[line][number-1] > file_input[line][number] \
                        and file_input[line-1][number] > file_input[line][number]:
                    lowest_numbers.append([file_input[line][number], line, number])

print(lowest_numbers)

sum = 0

for i in lowest_numbers:
    sum += int(i[0]) + 1

print(sum)
print(file_input)

