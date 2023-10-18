#ex7
def x_times(times,*lists):
    elements = []
    frv = []
    for ls in lists:
        for el in ls:
            ok = 1
            for i in range(0,len(elements)):
                if el == elements[i]:
                    frv[i] += 1
                    ok = 0
                    break

            if ok == 1:
                elements.append(el)
                frv.append(1)

    mylist = []
    for i in range(0,len(elements)):
        if frv[i] == times:
            mylist.append(elements[i])
    return mylist

print(x_times(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))
