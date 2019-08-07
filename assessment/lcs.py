# START TIME: 8:15pm


def get_matching_preceding_characters(i, j, matrix):
    if i - 1 < 0 or j - 1 < 0:
        return '', 0
    return matrix[i - 1][j - 1]


def lcs(x: str, y: str):
    matrix = [[0] * len(x) for _ in range(len(y))]
    max_len = 0
    longest_substring = ''
    for i, char_y in enumerate(y):
        for j, char_x in enumerate(x):
            if char_x == char_y:
                word, length = get_matching_preceding_characters(i, j, matrix)
                matrix[i][j] = (word + char_y, length + 1)
                if length + 1 >= max_len:
                    max_len, longest_substring = length + 1, word + char_y
            else:
                matrix[i][j] = '', 0

    return longest_substring


res = lcs('car', 'racecar')
print('res: ', res)
print(res == 'car')

# END TIME: 8:38pm
