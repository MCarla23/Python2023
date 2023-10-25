def validate_dict(rules, dt):
    ls = dict(map(lambda e: [e[0], (e[1], e[2], e[3])], rules))

    for key, val in dt.items():
        if key not in ls.keys():
            return False
        x = ls[key]
        if not val.startswith(x[0]):
            return False
        if not val.endswith(x[2]):
            return False
        if x[1] not in val[1:-1]:
            return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key2": "start middle winter"}))
