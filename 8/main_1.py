file_input = open("input.txt").readlines()
file_input = list(map(lambda s: s.strip(), file_input))
print(file_input)

for i in range(len(file_input)):
    file_input[i] = file_input[i].split(" | ")
    file_input[i][0] = file_input[i][0].split(" ")
    file_input[i][1] = file_input[i][1].split(" ")

for i in range(len(file_input[0])):
    for k in range(len(file_input[0][i])):
        file_input[0][i][k] = ''.join(sorted(file_input[0][i][k]))

current_segment = {
    "a": "",
    "b": "",
    "c": "",
    "e": "",
    "f": "",
    "g": "",
    }

numbers = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"]
}

current_segment_number = numbers

output_values = []

count = 0

for line in range(len(file_input)):
    current_segment_number = numbers
    for current_comb_len in range(1, 8):
        for current_number in range(len(file_input[line][0])):
            if len(file_input[line][0][current_number]) == current_comb_len:
                # if current_comb_len <= 4 or current_comb_len == 7:
                for key, value in numbers.items():
                    if len(value) == current_comb_len:
                        print(current_comb_len, "(=len)",
                              file_input[line][0][current_number], "(=input number)",
                              key, "(=output number)")
                        current_segment_number[key] = [current_segment_number[key],
                                                       list(file_input[line][0][current_number])]

for key, value in current_segment_number.items():
    print(key, ": ", end="")
    for i in value:
        if type(i) == list:
            print(i, end=" ")
        else:
            print(i, end="")

    print()

