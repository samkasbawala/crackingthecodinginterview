__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def zero_matrix(matrix: list) -> list:
    """If there is an element in an M x N matrix that is 0, this function will
    set its entire row or column to be 0

    Takes O(n^2) since we have to loop over all of the entries in the matrix
    """
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a bit vector
    rows_with_0 = 0
    cols_with_0 = 0

    for row in range(num_rows):
        for col in range(num_cols):
            # If it is a zero, mark it
            if matrix[row][col] == 0:
                rows_with_0 |= (1 << row)
                cols_with_0 |= (1 << col)

    # Set the appropriate rows to be all 0s
    for i in range(num_rows):
        if rows_with_0 & (1 << i) != 0:
            make_row_null(matrix, i)

    # Set the appropriate columns to be all 0s
    for i in range(num_cols):
        if cols_with_0 & (1 << i) != 0:
            make_col_null(matrix, i)

    # return the matrix
    return matrix


def make_row_null(matrix: list, row: int) -> None:
    """This function will make a specified row of a matrix all 0s"""
    for i in range(len(matrix[row])):
        matrix[row][i] = 0


def make_col_null(matrix: list, col: int) -> None:
    """This function will make a specified column of a matrix all 0s"""
    for row in matrix:
        row[col] = 0


class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        tests = [([[0, 1],
                  [1, 1]],

                  [[0, 0],
                   [0, 1]]),

                 ([[1, 2, 3, 4],
                   [5, 6, 7, 8]],

                  [[1, 2, 3, 4],
                   [5, 6, 7, 8]]),

                 ([[0, 0, 0],
                   [1, 1, 1],
                   [1, 1, 1]],

                  [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]])]

        for matrix, expected in tests:
            assert zero_matrix(matrix) == expected


if __name__ == '__main__':
    unittest.main()
