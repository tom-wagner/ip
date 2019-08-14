# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(U, L, C):
    # write your code in Python 3.6
    if sum(C) != U + L:
        return 'IMPOSSIBLE'
    row_one_sum = row_two_sum = 0
    matrix = [[0 for _ in C] for _ in range(0, 2)]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if C[j] == 2:
                matrix[i][j] = 1
                if i == 0:
                    row_one_sum += 1
                elif i == 1:
                    row_two_sum += 1
            elif i == 0 and row_one_sum < U and C[j] == 1:
                matrix[i][j] = 1
                row_one_sum += 1
            elif i == 1 and row_two_sum < L and matrix[i - 1][j] == 0 and C[j] == 1:
                matrix[i][j] = 1
                row_two_sum += 1
    arr_of_strings = [''.join(map(str, row)) for row in matrix]
    return ','.join(arr_of_strings)


print(solution(3, 2, [2, 1, 1, 0, 1]))

