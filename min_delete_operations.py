def get_adjacent_edit_distances(matrix, i, j):
    if i == 0 and j == 0:
        return 0, 0

    cell_to_left = matrix[i][j - 1]
    cell_above = matrix[i - 1][j]

    if i == 0:
        return cell_to_left, cell_to_left
    if j == 0:
        return cell_above, cell_above

    return cell_to_left, cell_above


def min_delete_operations(word1, word2):
    matrix = [[None for _ in word2] for _ in word1]

    for i, char_from_a in enumerate(word1):
        already_used_letter = False
        for j, char_from_b in enumerate(word2):
            if i == 0 and j == 0:
                matrix[i][j] = 0 if char_from_a == char_from_b else 2
                continue
            left, top = get_adjacent_edit_distances(matrix, i, j)

            if char_from_a == char_from_b and not already_used_letter:
                matrix[i][j] = min(left, top) - 1
                already_used_letter = True
            else:
                matrix[i][j] = min(left, top) + 1

    return matrix[len(word1) - 1][len(word2) - 1]


print(min_delete_operations('race', 'tree'))
