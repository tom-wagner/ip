# START TIME: 6:51pm


def lcs(x: str, y: str):
    matrix, longest = [[0 for _ in range(len(y))] for _ in range(len(x))], ''
    for i, char_x in enumerate(x):
        for j, char_y in enumerate(y):
            if char_x == char_y:
                preceding_length = matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                new_length = preceding_length + 1
                matrix[i][j] = new_length
                if new_length > len(longest):
                    longest = x[i - preceding_length:i + 1]
    return longest


res = lcs('car', 'racecar')

print('res: ', res)
print(res == 'car')

# END TIME: 7:01pm
