file_input = open("input.txt").readlines()

file_input = list(map(lambda x: x.strip(), file_input))

print(file_input)

parentheses = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

# scoring_table = {
#     ")": 3,
#     "]": 57,
#     "}": 1197,
#     ">": 25137
# }
# score = 0

scoring_table = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

score = []

for line in range(len(file_input)):
    error_in_line = False
    stack = []
    for character in range(len(file_input[line])):
        if file_input[line][character] in parentheses.keys():
            stack.append(file_input[line][character])
        else:
            if stack[-1] == \
                    list(parentheses.keys())[list(parentheses.values()).index(file_input[line][character])]:
                stack.pop()
            else:
                error_in_line = True
                # print("error on line {}: {} expected {} except got {}".format(line, file_input[line],
                #                                                               parentheses[stack[-1]],
                #                                                               file_input[line][character]))
                # score += scoring_table[file_input[line][character]]
                break
    if not error_in_line:
        line_score = 0
        stack.reverse()
        for i in range(len(stack)):
            stack[i] = parentheses[stack[i]]
        print(stack)
        for i in range(len(stack)):
            line_score *= 5
            line_score += scoring_table[stack[i]]
        score.append(line_score)
        print(line_score)

# print(score)
score.sort()
print(score[round(len(score)/2)-1])
