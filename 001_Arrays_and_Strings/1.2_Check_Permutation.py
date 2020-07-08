__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def is_permutation(string1: str, string2: str) -> bool:
    """Determines whether or not two strings are permutations of the other"""

    # Cannot be permutations if they are different lengths
    if len(string1) != len(string2):
        return False

    # Dictionary to keep track of number of each char
    chars = {}

    # Add each char in string1 to the dictionary, keep track of count
    for char in string1:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1

    # Loop through char in string2, char must be a key in the dict
    for char in string2:
        if char not in chars.keys():
            return False
        chars[char] -= 1

    # All values in dictionary MUST be 0, meaning we saw all characters
    # appropriate number of times
    return set([0]) == set(chars.values())


class TestIsPermutation(unittest.TestCase):
    def test_is_permutation_false(self):
        assert is_permutation('abcd', 'abce') is False
        assert is_permutation('abcd', 'abc') is False
        assert is_permutation('here', 'hear') is False
        assert is_permutation('two words', 'two_words') is False
        assert is_permutation('aaaaa', 'aa') is False
        assert is_permutation('test', 'testing') is False

    def test_is_permutation_true(self):
        assert is_permutation('abcd', 'dcba') is True
        assert is_permutation('sams', 'mass') is True
        assert is_permutation('wasd', 'wdsa') is True
        assert is_permutation('same', 'same') is True
        assert is_permutation('earth', 'heart') is True
        assert is_permutation('love', 'evol') is True


if __name__ == '__main__':
    unittest.main()
