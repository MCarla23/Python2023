def set_to_string(sett):
    stg = "{"
    for x in sett:
        stg += f"{x}, "
    stg = stg[:-2] + "}"
    return stg


def dict_op(*sets):
    dt = {}
    for ix, x in enumerate(sets):
        for iy, y in enumerate(sets):
            if iy <= ix:
                continue
            dx = set_to_string(x)
            dy = set_to_string(y)
            dt[dx + " | " + dy] = x | y
            dt[dx + " & " + dy] = x & y
            dt[dx + " - " + dy] = x - y
            dt[dy + " - " + dx] = y - x
    return dt


print(dict_op({1, 2}, {2, 3}))
