file_input = open("16_input.txt").readline()

conversion = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

bin_input = ""

for char in file_input:
    bin_input += conversion[char]

print(file_input)


def type_4(inf_bits: str = ""):
    message = ""
    length = 0
    while True:
        length += 1
        message += inf_bits[1:5]
        if inf_bits[0] == "0":
            break
        inf_bits = inf_bits[5:]
    print("message in binary: ", message)
    message = str(int(message, 2))
    print("message: ", message, "\n", "length in packets: ", length)
    return message, length


def other_type(inf_bits: str = ""):
    id_length = inf_bits[0]
    inf_bits = inf_bits[1:]

    if id_length == "1":
        print("id length: ", id_length)
        return other_type_1(inf_bits)
    else:
        return other_type_0(inf_bits)


def other_type_1(inf_bits: str = ""):
    num_of_packets = inf_bits[:11]
    num_of_packets = int(num_of_packets, 2)
    message = ""
    inf_bits = inf_bits[11:]
    print("information string: ", inf_bits)
    print("number of packets", num_of_packets)
    for i in range(num_of_packets):
        info = packet(inf_bits)
        length = int(info[1])
        message += info[0]
        inf_bits = inf_bits[length*5+6:]
    return message


def other_type_0(inf_bits: str = ""):
    length_of_packets = inf_bits[:15]
    length_of_packets = int(length_of_packets, 2)
    message = []
    length = 0
    inf_bits = inf_bits[15:]
    print("information string: ", inf_bits)
    print("length of packets", length_of_packets)
    while True:
        info = packet(inf_bits)
        length += int(info[1]) * 5 + 6
        message.append(info[0])
        inf_bits = inf_bits[int(info[1]) * 5 + 6:]
        print("total length: ", length)
        if length == length_of_packets:
            break
    return message


def packet(string: str = ""):
    print(string)
    version = string[:3]
    version = int(version, 2)
    global version_sum
    version_sum += version
    print()
    print("version: ", version)
    string = string[3:]

    id_type = string[:3]
    id_type = int(id_type, 2)
    print("id: ", id_type)
    string = string[3:]

    if id_type == 4:
        return type_4(string)
    else:
        return other_type(string)


version_sum = 0
print("\n"*5, "message: ", packet(bin_input))
print(version_sum)
