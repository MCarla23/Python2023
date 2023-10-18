#ex8
def ascii_code(x = 1, ls = [], flag = True):
    good_lists = []
    for s in ls:
        good_ascii = []
        for c in s:
            if flag == True:
                if ord(c) % x == 0:
                    good_ascii.append(c)
            elif ord(c) % x == 1:
                    good_ascii.append(c)
        if good_ascii != []:
            good_lists.append(good_ascii)
    return good_lists


print(ascii_code(2, ["test", "hello", "lab002"], False))