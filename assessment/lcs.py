# START TIME: 11:35am


def get_preceding_substring_length(i, j, matrix):
    if i == 0 or j == 0:
        return 0
    return matrix[i - 1][j - 1]


def lcs(x: str, y: str):
    matrix = [[0] * len(y) for _ in x]
    longest = ''
    for i, char_left in enumerate(x):
        for j, char_top in enumerate(y):
            if char_left == char_top:
                substring_length = get_preceding_substring_length(i, j, matrix) + 1
                matrix[i][j] = substring_length
                if substring_length >= len(longest):
                    longest = x[i + 1 - substring_length:i + 1]
    return longest


#   R A C E C A R
# C 0 0 1 0 1 0 0
# A 0 1 0 0 0 2 0
# R 1 0 0 0 0 0 3


res = lcs('dsfadsfascsd', 'dsfjlsadijfasdoheaoiwgbhwa')

print('res: ', res)
print(res == 'car')

# END TIME: 11:57am
