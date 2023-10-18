# ex1
def greatest_common_divisor():
    a = input("Introduceti primul numar: ")
    x = int(a)
    b = input("Introduceti al doilea numar: ")
    y = int(b)
    while y != 0:
        r = x % y
        x = y
        y = r

    print(f'Cel mai mare divizor dintr {a} si {b} este: {x}')
    return x


def loop_input():
    answer = "yes"
    while answer == "yes":
        greatest_common_divisor()
        print('Pentru da introduceti "yes", altfel orice introduceti o sa fie considerat nu.')
        answer = input('? Doriti sa continuati: ')


# ex2
def how_many_vowels(text):
    nrv = 0
    vocale = "aeiouAEIOU"
    for x in text:
        if vocale.find(x) != -1:
            nrv += 1
    print(f'Numarul de vocale din "{text}" este: {nrv}')
    return nrv


# ex3
def how_many_times(text1, text2):
    nrocc = text2.count(text1)
    print(f'Numarul de aparitii ale lui "{text1}" in "{text2}" este: {nrocc}')
    return nrocc


# ex4
def to_lower_case(text):
    slc = ""
    for x in text:
        if x.isupper():
            slc = slc + "_" + x.lower()
        else:
            slc = slc + x
    slc = slc[1:]
    print(f'To lower case & _: {slc}')
    return slc


# ex5
def spiral_matrix(matrix):
    lgmax = len(matrix)
    lg = len(matrix)
    x = 0
    y = 0
    i = 0
    d = 1
    while i < lgmax*lgmax:
        print(matrix[x][y], end="")
        i += 1
        if y == lg - 1 and d == 1:
            d = 2
            x = x + 1
        elif x == lg - 1 and d == 2:
            d = 3
            y = y - 1
        elif y == lgmax - lg and d == 3:
            d = 4
            x = x - 1
            lg = lg - 1
        elif x == lgmax - lg and d == 4:
            d = 1
            y = y + 1
        elif d == 1:
            y = y + 1
        elif d == 2:
            x = x + 1
        elif d == 3:
            y = y - 1
        elif d == 4:
            x = x - 1


# ex6
def is_palindrom(x):
    if x < 10:
        return True
    y = 0
    p = 1
    while p < x:
        y = y * 10 + x % 10
        x = x // 10
        p = p * 10
    if x == y or x == y // 10:
        return True
    print(f'x={x},y={y},p={p}')
    return False


# ex7
def extract_number(text):
    numbers = "0123456789"
    okay = 0
    for letter in text:
        if okay == 0 and numbers.find(letter) != -1:
            x = int(letter)
            okay = 1
        elif okay == 1 and numbers.find(letter) == -1:
            break
        elif okay == 1:
            x = x * 10 + int(letter)
    print(f'Primul numar din text este: {x}')
    return x


# ex8
def how_many_1(y):
    x = y
    nr = 0
    while x != 0:
        if x % 2 == 1:
            nr += 1
        x = x // 2
    print(f'Numarul de biti de 1 din {y} este: {nr}')
    return nr


# ex9
def highest_letter_occ(text):
    f = [0 for i in range(27)]
    maxi = 0
    maxLetter = '-'
    text = text.lower()
    for letter in text:
        if letter >= 'a' and letter <= 'z':
            f[ord(letter) - ord('a')] += 1
            if f[ord(letter) - ord('a')] > maxi:
                maxi = f[ord(letter) - ord('a')]
            maxLetter = letter

    print(f'Litera "{maxLetter}" apare de cele mai multe ori in textul "{text}". Mai precis, de {maxi} ori.')
    return maxi


# ex10
def how_many_words(text):
    nr = 0
    space = text.find(" ")
    while space != -1:
        if space > 0:
            if text[space - 1].isalpha():
                nr += 1
        text = text[(space+1):]
        space = text.find(" ")

    for letter in text:
        if letter.isalpha():
            nr += 1
            break

    print(f'In acest text sunt {nr} cuvinte.')
    return nr


#loop infinit
while True:
    print(" ")
    ex = input("Introduceti numarul exercitiului pe care vreti sa il testati: ")

    if ex == "1":
        loop_input()
    elif ex == "2":
        how_many_vowels("Ana are mere.")
    elif ex == "3":
        how_many_times("ca", "abcabcabcabc")
    elif ex == "4":
        to_lower_case("AA")
    elif ex == "5":
        spiral_matrix(["firs", "n_lt", "oba_", "htyp"])
    elif ex == "6":
        print('')
        print('Am I a palindrom?...', is_palindrom(23432))
    elif ex == "7":
        extract_number("An apple is 123 USD")
        extract_number("abc123abc1234")
    elif ex == "8":
        how_many_1(0)
        how_many_1(1)
        how_many_1(2)
        how_many_1(3)
        how_many_1(7)
        how_many_1(24)
    elif ex == "9":
        highest_letter_occ("an apple is not a tomato")
    elif ex == "10":
        how_many_words("I have Python exam")
    else:
        loop_input()
        how_many_vowels("Ana are mere.")
        how_many_times("apex", "Hana teul apex triapex apexapex manifest")
        to_lower_case("CamilaMeaFrumoasa")
        spiral_matrix(["firs", "n_lt", "oba_", "htyp"])
        print('')
        print('Am I a palindrom?...', is_palindrom(23432))
        extract_number("An apple is 123 USD")
        extract_number("abc123abc")
        how_many_1(0)
        how_many_1(1)
        how_many_1(2)
        how_many_1(3)
        how_many_1(7)
        how_many_1(24)
        highest_letter_occ("an apple is not a tOmato")
        how_many_words("I have Python exam")
