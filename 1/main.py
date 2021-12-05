import time

file = open("input.txt").readlines()
file = list(map(int, file))
count = 0
start = 0
sum = 0
old_sum = 9999999


for i in range(len(file)-2):
    sum = 0
    for i in range(3):
        sum += file[start + i]
    if sum > old_sum:
        count += 1

    #  print(old_sum, sum, old_sum < sum, count)
    start += 1
    old_sum = sum
    #  time.sleep(2)

print(count)
