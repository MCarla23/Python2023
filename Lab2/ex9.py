#ex9
def spectators(stadion):
    nv = []
    l = len(stadion)
    c = len(stadion[0])
    maxis = []
    for j in range(0, c):
        maxis.append(0)
        for i in range(0, l):
            if stadion[i][j] <= maxis[j]:
                nv.append((i,j))
            else:
                maxis[j] = stadion[i][j]
    return nv


print(spectators([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]] ))
