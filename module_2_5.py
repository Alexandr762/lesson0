def get_matrix(n, m, value):
    matrix = []

    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

matrix = get_matrix(78, 45, ' fox ')
print(matrix)