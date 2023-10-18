#ex7
def is_palindrom(x):
    if x < 10:
        return 1
    y = 0
    p = 1
    while p < x:
        y = y * 10 + x % 10
        x = x // 10
        p = p * 10
    if x == y or x == y // 10:
        return 1
    return 0


def palindroms(numbers):
    nr = 0
    maxi = -1
    for x in numbers:
        if is_palindrom(x) == 1:
            nr += 1
            if x > maxi:
                maxi = x
    return (nr,maxi)


print(palindroms([252,153645,3445,232,999,7887,343,276367]))