# START TIME: 6:07pm


def get_adjacent_cells(matrix, i, j):
    default = dict(value=0, string='')
    cell_left = matrix[i][j - 1] if i >= 0 and j - 1 >= 0 else default
    cell_top = matrix[i - 1][j] if i - 1 >= 0 and j >= 0 else default
    cell_top_left = matrix[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else default
    return cell_left, cell_top, cell_top_left


def lcs(x: str, y: str):
    word_one_arr, word_two_arr = ([char for char in word] for word in (x, y))

    matrix = [[None for _ in word_one_arr] for _ in word_two_arr]

    for i, left_char in enumerate(word_two_arr):
        for j, top_char in enumerate(word_one_arr):
            cell_left, cell_top, cell_top_left = get_adjacent_cells(matrix, i, j)
            if left_char == top_char:
                matrix[i][j] = dict(value=cell_top_left['value'] + 1, string=cell_top_left['string'] + left_char)
            else:
                matrix[i][j] = cell_left if cell_left['value'] >= cell_top['value'] else cell_top

    return matrix[len(word_two_arr) - 1][len(word_one_arr) - 1]['string']


res = lcs('racecar', 'care')

print('res: ', res)
print(res == 'car')

# END TIME: 6:48pm
