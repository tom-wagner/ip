import random


def zero_matrix(matrix):
    rows_to_zero_out, columns_to_zero_out = set(), set()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                rows_to_zero_out.add(i)
                columns_to_zero_out.add(j)

    print(rows_to_zero_out)
    print(columns_to_zero_out)

    for i, row in enumerate(matrix):
        if i in rows_to_zero_out:
            matrix[i] = [0 for _ in range(len(row))]
        for j, val in enumerate(row):
            if j in columns_to_zero_out:
                matrix[i][j] = 0

    return matrix


a = [[random.randint(0, 20) for _ in range(10)] for _ in range(10)]
