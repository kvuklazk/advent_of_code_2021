def print_list(list_to_print, biggest_len=2, lowest_len=1):
    if type(list_to_print[0]) == "str":
        list_to_print = list(map(lambda x: x.strip(), list_to_print))
    for line_to_print in list_to_print:
        str_to_print = ''
        for char_to_print in line_to_print:
            if len(str(char_to_print)) == lowest_len:
                str_to_print += str(char_to_print)
                for i in range(biggest_len-lowest_len+1):
                    str_to_print += " "
            else:
                str_to_print += "{} ".format(str(char_to_print))
        print(str_to_print, "...")
