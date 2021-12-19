input_file = open("input.txt").readline()

input_file = input_file.split(",")
input_file = list(map(int, input_file))
input_file.sort()


print(input_file)

mean = input_file[round(len(input_file)/2)]
print(mean)

sum_answer = 0

for i in input_file:
    sum_answer += abs(mean - i)

print(sum_answer)
