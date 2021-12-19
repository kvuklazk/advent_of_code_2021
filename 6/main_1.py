file_input = open("input.txt").readline()
file_input = file_input.split(',')
file_input.sort()
print("Initial state: {}".format(", ".join(file_input)))
file_input = list(map(int, file_input))


fishe = []

for i in range(9):
    fishe.append([i, 0])

for i in file_input:
    fishe[i][1] += 1

print(fishe)

for i in range(256):
    new_fish = 0
    for k in range(len(fishe)):
        if fishe[k][1] != 0:
            if fishe[k][0] != 0:
                fishe[k-1][1] += fishe[k][1]
                fishe[k][1] -= fishe[k][1]
            else:
                new_fish += fishe[k][1]
    fishe[6][1] += new_fish
    fishe[8][1] += new_fish
    fishe[0][1] -= new_fish

    # print(fishe)
    # print("After  {:n} day: ".format(i + 1), end="")
    # for p in range(len(fishe)):
    #     for k in range(fishe[p][1]):
    #         print(fishe[p][0], end=", ")
    # print()

answer_sum = 0

for i in fishe:
    answer_sum += i[1]

print("\n" * 2, answer_sum)
