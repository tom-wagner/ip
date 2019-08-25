from copy import copy

class Spreadsheet:
    def __init__(self, rows: int, columns: int):
        self.sheet = [['' for _ in range(0, columns)] for _ in range(0, rows)]

    def update_cell(self, value: any, r: int, c: int):
        error_message = 'Please pass a valid cell index'
        if r < 0 or c < 0:
            return 'Please pass a valid cell index'
        try:
            self.sheet[r][c] = value
        except IndexError:
            return error_message

    def print(self, matrix_to_print=None):
        # transform each row into a string with | between each cell
        # print out those rows with newlines
        if not matrix_to_print:
            matrix_to_print = self.sheet
        strings = ["|".join(map(str, row)) for row in matrix_to_print]
        print("\n".join(strings))

    def pretty_print(self):
        longest_elem_in_each_column = []
        num_rows, num_cols = len(self.sheet), len(self.sheet[0])

        for c in range(0, num_cols):
            longest_elem_in_column = 0
            for r in range(0, num_rows):
                print(r, c)
                current_element_length = len(str(self.sheet[r][c]))
                longest_elem_in_column = max(longest_elem_in_column, current_element_length)
            longest_elem_in_each_column.append(longest_elem_in_column)

        print(longest_elem_in_each_column)

        matrix_copy = copy(self.sheet)

        for c in range(0, num_cols):
            for r in range(0, num_rows):
                # 8
                # 3
                current_element_length = len(str(self.sheet[r][c]))
                whitespace_to_add = (longest_elem_in_each_column[c] - current_element_length) * ' '
                element_to_add_to_matrix = str(self.sheet[r][c]) + whitespace_to_add
                matrix_copy[r][c] = element_to_add_to_matrix

        self.print(matrix_copy)


s = Spreadsheet(3, 5)
# print(s.sheet)

s.update_cell('a string', 1, 1)

s.update_cell('abc', 0, 1)

# print(s.sheet)

# s.print()

s.pretty_print()




