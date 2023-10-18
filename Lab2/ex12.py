#ex12
def rhyme(ls):
    groups = []
    for word in ls:
        sufix = word[len(word)-2:]
        ok = 0
        for ig in range(0,len(groups)):
            if groups[ig][0][len(groups[ig][0])-2:] == sufix:
                groups[ig].append(word)
                ok = 1
        if ok == 0:
            groups.append([word])
    return groups


print(rhyme(["ana","banana","carte","arme","parte","na"]))