# START TIME: 10:28pm


def lcs(x: str, y: str):
    matrix = [[0] * len(y) for _ in x]
    lcs_last_char_idx = None
    max_len = 0

    for r, char_x in enumerate(x):
        for c, char_y in enumerate(y):
            if char_x == char_y:
                if r == 0:
                    lcs_last_char_idx = r
                    max_len = 1
                else:
                    curr_len = matrix[r - 1][c - 1] + 1
                    matrix[r][c] = curr_len
                    if curr_len > max_len:
                        max_len = curr_len
                        lcs_last_char_idx = r
            else:
                matrix[r][c] = 0

    return x[lcs_last_char_idx - max_len:lcs_last_char_idx + 1]


res = lcs('car', 'racecar')

print('res: ', res)
print(res == 'car')

#    r a c e c a r
# c  0 0 1 0 1 0 0
# a  0 1 0 0 0 2 0
# r  1 0 0 0 0 0 3

# END TIME: 10:37pm
