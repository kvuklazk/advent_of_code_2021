file = open("message.txt").readlines()

#  1, 0

gama_rate = []
gama_rate_final = ''


for i in range(len(file[0])-1):
    gama_rate.append([0, 0])

for i in file:
    for k in range(len(i)-1):
        if i[k] == '1':
            gama_rate[k][0] += 1
        else:
            gama_rate[k][1] += 1

for i in gama_rate:
    if i[0] > i[1]:
        gama_rate_final += '1'
    else:
        gama_rate_final += '0'

epsilon_rate = ''

for i in gama_rate_final:
    if i == '1':
        epsilon_rate += '0'
    else:
        epsilon_rate += '1'


print(int(gama_rate_final, 2), int(epsilon_rate, 2), int(gama_rate_final, 2) * int(epsilon_rate, 2))

