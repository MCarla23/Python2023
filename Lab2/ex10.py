#ex10
def same_position(*lists):
    mls = []
    lmaxi = 0
    for ls in lists:
        if len(ls) > lmaxi:
            lmaxi = len(ls)
        mls.append([])

    for ils in range(0,len(lists)):
        lenls = len(lists[ils])
        for i in range(0,lmaxi):
            if i < lenls:
                mls[ils].append(lists[ils][i])
            else:
                mls[ils].append(None)
    return mls


print(same_position([1,2], [5,6,7,8], ["a", "b", "c"]))