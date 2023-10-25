def unique_and_duplicate(ls):
    sa = set(filter(lambda e: ls.count(e) == 1, ls))
    sb = set(ls) - sa
    return (len(sa), len(sb))


print(unique_and_duplicate([1, 8, 4, 3, 2, 2, 1, 8, 8, 10, 11, 8, 34]))
