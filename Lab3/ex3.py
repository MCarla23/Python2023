def compare_lists_tuples(l1,l2):
    if len(l1) != len(l2):
        return False
    if isinstance(l1, set):
        l1 = list (l1)
        l2 = list (l2)
        l1.sort(key=lambda e: str(e))
        l2.sort(key=lambda e: str(e))

    for i in range(0, len(l1)):
        if not isinstance(l1[i], type(l2[i])):
            return False

        if isinstance(l1[i], (list, tuple, set)):
            return compare_lists_tuples(l1[i], l2[i])
        elif isinstance(l1[i], dict):
            return compare_dict(l1[i], l2[i])
        elif l1[i] != l2[i]:
            return False
    return True


def compare_dict(d1, d2):
    if d1.keys() != d2.keys():
        return False
    for k in d1.keys():
        if not isinstance(d1[k], type(d2[k])):
            return False

        if isinstance(d1[k], (list,tuple,set)):
            return compare_lists_tuples(d1[k], d2[k])
        elif isinstance(d1[k], dict):
            return compare_dict(d1[k],d2[k])
        elif d1[k] != d2[k]:
            return False
    return True


print(compare_dict({"ana": [2, 3, [4]]}, {"ana": [2, 3, [4]]}))
print(compare_dict({"ana": [2, 3, 4]}, {"ana": [2, 3, [4]]}))
print(compare_dict({"ana": [2, 3, [4]]}, {"ana": [2, 3, [4]], "x": 2}))
print(compare_dict({"k1": {2,3,4}},{"k1": {2,4,"3"}}))
