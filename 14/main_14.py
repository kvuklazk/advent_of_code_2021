import time

input_file = open("input.txt").readlines()

input_file = [line.rstrip() for line in input_file]

field = input_file[0]
field = list(field)
input_file.pop(0)
input_file.pop(0)

for line in range(len(input_file)):
    input_file[line] = [input_file[line][:2], input_file[line][-1]]

rules = {}
for rule in input_file:
    rules[rule[0]] = rule[1]
print(rules)

print("after 0 steps: ", "".join(field))

# for step in range(40):
#     pair = 0
#     while True:
#         # print(field[pair], field[pair+1])
#         if field[pair] + field[pair+1] in rules:
#             field.insert(pair+1, rules[field[pair] + field[pair+1]])
#             pair += 1
#         pair += 1
#         if pair == len(field)-1 or pair > len(field)-1:
#             break
#     print(step)
#     # print("after {} steps: ".format(step+1), "".join(field))

field = "".join(field)
forbidden_index = []
for step in range(40):
    final_field = field
    for rule in rules.items():
        for i in range(1):
            if rule[0] in field:
                final_field = final_field.replace(rule[0], rule[0][0] + rule[1] + rule[0][1])
                forbidden_index.append(final_field.find(rule[0][0] + rule[1] + rule[0][1])+1)
            else:
                break
    # TODO how not to insert in new element
    # print(final_field)
    print(step)
    # print("after {} steps: ".format(step+1), "".join(field))
else:
    print("after {} steps: ".format(step+1), "".join(field))

common = {}
for char in field:
    if char not in common:
        common[char] = 1
    else:
        common[char] += 1

max_common = 0
min_common = 0

for key, value in common.items():
    if max_common == 0:
        max_common = value
        min_common = value
    if value < min_common:
        min_common = value
    if value > max_common:
        max_common = value
print(min_common, max_common, max_common-min_common)
