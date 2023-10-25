def positional_arguments(*pa, **kw):
    nr = 0
    for x in pa:
        if x in kw.values():
            nr += 1
    return nr


print(positional_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5))
