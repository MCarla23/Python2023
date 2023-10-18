#ex3
def lists_fun(a,b):
    intersectie = []
    aminusb = []
    reuniune = []

    for x in a:
        if x in b:
            intersectie.append(x)
        else:
            aminusb.append(x)
            reuniune.append(x)

    reuniune.extend(b)
    bminusa = []

    for x in b:
        if x not in intersectie:
            bminusa.append(x)
    print(f'Avem multimile {a} si {b}.')
    print(f'Reuniunea lor este {reuniune}.')
    print(f'Intersectia lor este {intersectie}.')
    print(f'a - b este {aminusb}.')
    print(f'b - a este {bminusa}.')


lists_fun([43,23,10,44,34,2,1],[1,99,22,23,14,15])