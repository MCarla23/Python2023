def ch_count(s):
    dt = {x: s.count(x) for x in set(s)}
    return dt


print(ch_count("Ana has apples."))
