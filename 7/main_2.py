input_file = open("input.txt").readline()

input_file = input_file.split(",")
input_file = list(map(int, input_file))
input_file.sort()


print(input_file)

average = int(round(sum(input_file) / len(input_file)-0.5))
print(average)

sum_answer = 0
# best_answer = 0
# for k in range(input_file[-1]):
#     best_answer += k + 1
# best_answer *= len(input_file)
# position = 0

# for l in range(input_file[-1] + 1):
#     sum_answer = 0
#     for i in input_file:
#         for k in range(abs(l - i)):
#             sum_answer += k+1
#     print(sum_answer, best_answer, l)
#     if sum_answer < best_answer:
#         best_answer = sum_answer
#         position = l

for i in input_file:
    for k in range(abs(average - i)):
        sum_answer += k + 1

print(sum_answer)
