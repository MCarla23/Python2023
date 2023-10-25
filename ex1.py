def list_of_sets(a, b):
    sa = set(a)
    sb = set(b)
    return [sa & sb, sa | sb, sa - sb, sb - sa]


print(list_of_sets([1, 2, 3],[2, 7, 9]))