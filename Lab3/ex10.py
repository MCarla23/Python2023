def dict_mapping(mapping):
    fr = []
    current = "start"
    while current not in fr:
        fr.append(current)
        current = mapping[current]
    return fr[1:]


print(dict_mapping({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))