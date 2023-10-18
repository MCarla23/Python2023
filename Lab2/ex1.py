#ex1
def fibo(n):
    if n == 0:
        print(f'Primul numar din Fibonacci este: [0]')
        return [0]
    if n == 1:
        print(f'Primele {n} numere din Fibonacci sunt: [0,1]')
        return [0,1]

    ls = [0,1]
    i = 2
    while i < n:
        ls.append(ls[i-1]+ls[i-2])
        i += 1
    print(f'Primele {n} numere din Fibonacci sunt: {ls}')

    return ls

fibo(8)