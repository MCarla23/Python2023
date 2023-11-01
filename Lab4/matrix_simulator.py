class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(n):
            line = []
            for j in range(m):
                line.append(0)
            self.matrix.append(line)

    def get_element(self, i, j):
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        self.matrix[i][j] = value

    def set_matrix(self, mat):
        for i in range(self.n):
            for j in range(self.m):
                self.set_element(i, j, mat[i][j])

    def get_matrix(self):
        return self.matrix

    def get_transpusa(self):
        tran = []
        for i in range(self.m):
            line = []
            for j in range(self.n):
                line.append(self.matrix[j][i])
            tran.append(line)
        return tran

    def multiply_with(self, mat):
        multi = Matrix(self.n, len(mat[0]))

        if self.m != len(mat):
            return None
        for i in range(self.n):
            for j in range(self.m):
                for k in range(len(mat[0])):
                    multi.set_element(i, k, multi.get_element(i, k) + self.get_element(i, j) * mat[j][k])
        return multi.matrix

    def apply_function(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.set_element(i, j, func(self.get_element(i,j)))
        return self.matrix


matrice = Matrix(3,3)
mat2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrice.set_matrix(mat2)
print(matrice.get_transpusa())
print(matrice.multiply_with(matrice.get_transpusa()))
print(matrice.apply_function(lambda x: x*x))
