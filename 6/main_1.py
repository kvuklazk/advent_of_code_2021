file_input = open("input.txt").readline()


print("Initial state: {}".format(file_input))

file_input = file_input.split(',')
file_input = list(map(int, file_input))

for i in range(256):
    new_fish = []
    for k in range(len(file_input)):
        if file_input[k] != 0:
            file_input[k] -= 1
        else:
            file_input[k] = 6
            new_fish.append(8)
    for k in new_fish:
        file_input.append(k)
    print(i, file_input)
    # print("After  {:n} day:  {}".format(int(i + 1), file_input))

print("\n" * 10, len(file_input))

# napsat to tak ze novy ryby jsou vsechny jako list [stav, pocet]
