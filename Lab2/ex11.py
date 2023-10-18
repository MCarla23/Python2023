#ex11
def fromTuple(tuple):
    return tuple[1][2]


def tuples(ls):
    ls.sort(key = fromTuple)
    return ls

print(tuples([('abc','bcd'),('abc','zza')]))