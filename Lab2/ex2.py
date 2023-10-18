#ex2
def is_prime(x):
    if x == 0 or x == 1:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    for d in range(3, x // 2, 2):
        if x % d == 0:
            return 0
    return 1


def prime_list(ls):
    lsp = []
    for x in ls:
        if is_prime(x) == 1:
            lsp.append(x)
    print(f'Numerele prime din lista {ls} sunt: {lsp}')
    return lsp

prime_list([6,2,34,99,21,23,7,19,342,100])
