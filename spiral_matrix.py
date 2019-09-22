from typing import List


def gather_row(matrix, row_idx, left_col_idx, right_col_idx):
    return [el for el in matrix[row_idx][left_col_idx: right_col_idx + 1]]


def gather_column(matrix, col_idx, top_row_idx, bottom_row_idx):
    return [row[col_idx] for row in matrix[top_row_idx: bottom_row_idx + 1]]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            top_row = gather_row(matrix, top, left, right)
            right_side = gather_column(matrix, right, top + 1, bottom - 1)
            bottom_row = gather_row(matrix, bottom, left, right) if top < bottom else []
            left_side = gather_column(matrix, left, top + 1, bottom - 1) if left < right else []
            bottom_row.reverse()
            left_side.reverse()

            res.extend([*top_row, *right_side, *bottom_row, *left_side])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res
