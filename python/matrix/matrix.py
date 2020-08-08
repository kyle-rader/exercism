class Matrix:
    def __init__(self, matrix_string):
        self.orig = matrix_string

        self.matrix = []
        for row in matrix_string.split("\n"):
            self.matrix.append([int(val) for val in row.split()])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
