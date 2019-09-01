
# START TIME: 12:57pm


def lcs(x: str, y: str):
    matrix = [[0 for _ in y] for _ in x]
    max_len = 0
    y_idx = None

    for r, char_x in enumerate(x):
        for c, char_y in enumerate(y):
            if char_x == char_y:
                if r == 0:
                    matrix[r][c] = 1
                    curr_length, y_idx = 1, c
                else:
                    matrix[r][c] = matrix[r - 1][c - 1] + 1
                    curr_length = matrix[r][c]

                y_idx, max_len = (c, curr_length) if curr_length > max_len else (y_idx, max_len)

    if not y_idx:
        return ''

    first_char_idx, last_char_idx = y_idx - max_len + 1, y_idx
    return y[first_char_idx:last_char_idx + 1]


#   r a c e c a r
# c 0 0 1 0 1 0 0
# a 0 1 0 0 0 2 0
# r 1 0 0 0 0 0 3

res = lcs('car', 'racecar')

print('res: ', res)
print(res == 'car')

# END TIME: 1:12pm
