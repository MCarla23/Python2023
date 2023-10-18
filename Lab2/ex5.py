def matrix0(mat):
    for i in range(0,len(mat)):
        for j in range(0, len(mat[i])):
            if i > j:
                mat[i][j] = 0
    return mat


print(f'Matrice schimbata este: {matrix0([[8,3,4,5,6],[2,3,4,5,3],[3,4,5,3,9],[8,3,4,5,3]])}')
