file = open("message.txt").readlines()
file = list(map(str.strip, file))

#  1, 0

gama_rate = ""

for digit in range(len(file[0])):
    digits = []
    for i in file:
        digits.append(i[digit])
    sum_1 = 0
    sum_0 = 0
    for i in digits:
        if i == "1":
            sum_1 += 1
        else:
            sum_0 += 1
    if sum_1 > sum_0:
        gama_rate += "1"
    else:
        gama_rate += "0"

epsilon_rate = ""

for i in gama_rate:
    if i == "1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

print(gama_rate, epsilon_rate)
file_copy = file.copy()

while len(file_copy) > 1:
    print(file_copy)
    for digit in range(len(file[0])):
        digits = []
        numbers_to_remove = []
        for i in range(len(file_copy)):
            if file_copy[i][digit] != gama_rate[digit]:
                numbers_to_remove.append(file_copy[i])
        if len(file_copy) == 2:
            for i in file_copy:
                if i[digit] != "1":
                    file_copy.remove(i)
            break
        for i in numbers_to_remove:
            if i in file_copy:
                file_copy.remove(i)
        print(digit)

print(file_copy)
oxygen_generator_rating = file_copy[0]

file_copy = file.copy()
print(file_copy)

while len(file_copy) > 1:
    for digit in range(len(file[0])):
        digits = []
        numbers_to_remove = []
        for i in range(len(file_copy)):
            if file_copy[i][digit] != epsilon_rate[digit]:
                numbers_to_remove.append(file_copy[i])
        if len(file_copy) == 2:
            for i in file_copy:
                if i[digit] != "0":
                    file_copy.remove(i)
            break
        for i in numbers_to_remove:
            if len(file_copy) == 1:
                break
            if i in file_copy:
                file_copy.remove(i)
        print(digit)


CO2_scrubber_rating = file_copy[0]

oxygen_generator_rating_dec = int(oxygen_generator_rating, 2)
CO2_scrubber_rating_dec = int(CO2_scrubber_rating, 2)

life_support_rating = oxygen_generator_rating_dec * CO2_scrubber_rating_dec

print(oxygen_generator_rating, CO2_scrubber_rating)

print(life_support_rating, oxygen_generator_rating_dec, CO2_scrubber_rating_dec)


