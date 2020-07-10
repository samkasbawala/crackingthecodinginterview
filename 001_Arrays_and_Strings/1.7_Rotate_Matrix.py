__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasabwala'

import unittest

############################## MY FIRST ATTEMPT ##############################
def rotate(image: list, n: int) -> list:
    """This function rotates the image (represented by a two dimensional
    array) 90 degrees clockwise

    This function runs in O(n^2 + n^log(n)) = O(n^2log(n))
    """
    # Create an empty 2D list
    rotated = [[None for _ in range(n)] for _ in range(n)]

    # Create transpose of image
    for col in range(n):
        for row in range(n):
            rotated[col][row] = image[row][col]

    # Reverse each row in the transpose
    for row in rotated:
        row = row.reverse()

    return rotated

############################## MY SECOND ATTEMPT #############################
def rotate_2(image: list) -> list:
    """This function roatets the image (represented by a two dimensional
    array) 90 degrees clockwise

    This second attempt is better than the first since it does not use any
    extra space and is faster. This function runs in O(n^2).
    """
    # Get the length of the array
    n = len(image)
    for layer in range(n // 2):
        start, end = layer, n - layer - 1
        for index in range(start, end):
            # Save the top value
            top = image[layer][index]

            # Save left to top
            image[layer][index] = image[n - index - 1][layer]

            # Save bottom to left
            image[n - index - 1][layer] = image[n - layer - 1][n - index - 1]

            # Save right value to bottom
            image[n - layer - 1][n - index - 1] = image[index][n - layer - 1]

            # Save top to right
            image[index][n - layer - 1] = top

    # return the immage
    return image


class TestRotate(unittest.TestCase):
    def test_rotate(self):
        matrix = [['M', 'O', 'M'],
                  ['D', 'A', 'D'],
                  ['S', 'O', 'N']]
        assert rotate(matrix, 3) == [['S', 'D', 'M'],
                                     ['O', 'A', 'O'],
                                     ['N', 'D', 'M']]
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        assert rotate(matrix, 4) == [[13, 9, 5, 1],
                                     [14, 10, 6, 2],
                                     [15, 11, 7, 3],
                                     [16, 12, 8, 4]]

    def test_rotate_2(self):
        matrix = [['M', 'O', 'M'],
                  ['D', 'A', 'D'],
                  ['S', 'O', 'N']]
        assert rotate_2(matrix) == [['S', 'D', 'M'],
                                    ['O', 'A', 'O'],
                                    ['N', 'D', 'M']]
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        assert rotate_2(matrix) == [[13, 9, 5, 1],
                                    [14, 10, 6, 2],
                                    [15, 11, 7, 3],
                                    [16, 12, 8, 4]]


if __name__ == '__main__':
    unittest.main()
