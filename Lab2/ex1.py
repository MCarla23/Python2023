#ex1
def fibo(n):
    if n == 1:
        print(f'Primul numar din Fibonacci este: [1]')
        return [1]
    if n == 2:
        print(f'Primele {n} numere din Fibonacci sunt: [1,1]')
        return [1,1]
    a = 1
    b = 1
    ls = [1,1]
    i = 2

    while i < n:
        aux = a
        a = b
        b = aux + b
        ls.append(b)
        i += 1
    print(f'Primele {n} numere din Fibonacci sunt: {ls}')

    return ls

fibo(8)
