# START TIME: 4:13pm

#   r a c e c a r
# c 0 0 1 0 1 0 0
# a 0 1 0 0 0 2 0
# r 1 0 0 0 0 0 3


def lcs(x: str, y: str):
    max_len, lcs = 0, ''

    matrix = [[0 for _ in y] for _ in x]
    print(matrix)

    for i, char_x in enumerate(x):
        for j, char_y in enumerate(y):
            if char_x == char_y:
                substring_length = matrix[i - 1][j - 1] + 1 if i >= 1 and j >= 1 else 1
                if substring_length >= max_len:
                    max_len = substring_length
                    lcs = x[i - max_len + 1:i + 1]
                matrix[i][j] = substring_length
            else:
                matrix[i][j] = 0

    return lcs


res = lcs('car', 'racecar')

print('res: ', res)
print(res == 'car')

# END TIME: 4:24pm
