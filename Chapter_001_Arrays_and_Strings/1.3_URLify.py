__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def urlify(char_array: list or str, true_length: int) -> list:
    """Function will replace spaces in a string with '%20'. Assumes that the
    string has sufficient space at the end to hold the extra characters

    Runs in O(n) time since we just iterate throught the string.
    """
    if type(char_array) is str:
        char_array = list(char_array)

    # Index of new end
    new_end = (count_spaces(char_array, true_length) * 2) + true_length - 1
    if new_end < len(char_array) - 1:
        char_array = char_array[:new_end + 1]

    # Index of old end
    old_end = true_length - 1

    # Start from the end and loop backwards until old end and new end match
    while old_end != new_end:
        if char_array[old_end] != ' ':
            char_array[new_end] = char_array[old_end]
            new_end -= 1
            old_end -= 1
        else:
            char_array[new_end] = '0'
            char_array[new_end - 1] = '2'
            char_array[new_end - 2] = '%'
            new_end -= 3
            old_end -= 1

    return char_array


def count_spaces(char_array: list, true_length):
    count = 0
    for char in char_array[:true_length]:
        if char == ' ':
            count += 1
    return count


class TestURLify(unittest.TestCase):
    def test_urlify(self):
        assert urlify('Sam Kasbawala  ', 13) == list('Sam%20Kasbawala')
        assert urlify(list('Sam Kasbawala  '), 13) == list('Sam%20Kasbawala')

        assert urlify('Mr John Smith    ', 13) == list('Mr%20John%20Smith')
        assert urlify(list('Mr John Smith    '), 13) == list('Mr%20John%20Smith')

        assert urlify('      ', 2) == list('%20%20')
        assert urlify(list('      '), 2) == list('%20%20')

    def test_urlify_extra_whitespace(self):
        assert urlify('Sam Kasbawala    ', 13) == list('Sam%20Kasbawala')
        assert urlify(list('Sam Kasbawala    '), 13) == list('Sam%20Kasbawala')

        assert urlify('Mr John Smith     ', 13) == list('Mr%20John%20Smith')
        assert urlify(list('Mr John Smith     '), 13) == list('Mr%20John%20Smith')

        assert urlify('          ', 2) == list('%20%20')
        assert urlify(list('          '), 2) == list('%20%20')


if __name__ == '__main__':
    unittest.main()
