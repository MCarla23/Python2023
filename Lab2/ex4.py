#ex4
def compose_song(lsn, lsm, start):
    song = [lsn[start]]
    nxt = start
    lg = len(lsn)
    for x in lsm:
        nxt += x
        nxt = nxt % len(lsn)
        song.append(lsn[nxt])
    return song


print('Melodia mea: ', compose_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
