__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

from math import factorial
import unittest
import re


def is_palindrome_permutation(string: str) -> bool:
    """Checks if the inputted string is a permutation of a palindrome"""

    # Get permutations
    permutations = set(get_permutations(string))

    # Check for palindromes
    for permutation in permutations:
        if is_palindrome(permutation):
            return True
    return False


def get_permutations(string: str) -> set:
    """Function to get permutations of a string"""

    # String should only contain letters and case doesn't matter
    string = re.sub('[^a-zA-Z]', '', string)

    # Call the helper function to populate the set of permutations
    permutations = []
    permutation_helper(string.lower(), len(string), permutations)
    return permutations


def permutation_helper(string: str,
                       remaining: int,
                       permutations: list,
                       permutation: str = '') -> None:
    """Find all permutations of a given string"""

    # Used up all the letters
    if remaining == 0:
        permutations.append(permutation)
    else:
        for i in range(len(string)):
            permutation_helper(string[0:i] + string[i+1:],
                               remaining - 1,
                               permutations,
                               permutation + string[i])


def is_palindrome(string: str) -> bool:
    """Function to determine if a string is a palindrome

    Assumes that the inserted string does not contain any non alpha characters.
    i.e. There are no spaces, numbers, escaped characters, etc.
    """

    # Determine max index we need to check up to
    end = len(string) // 2 if len(string) % 2 == 0 else len(string) // 2 + 1

    # Loop through string
    for index in range(end):
        if string[index] != string[len(string) - 1 - index]:
            return False
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_is_palindrome(self):
        assert is_palindrome('kayak') is True
        assert is_palindrome('noon') is True
        assert is_palindrome('tacocat') is True

        assert is_palindrome('sam') is False
        assert is_palindrome('test') is False
        assert is_palindrome('two words') is False

    def test_get_permutations(self):
        # We can check permutations by checking the length of the list that
        # is returned. There factorial(len(string)) permutations (need not
        # be unique)

        assert len(get_permutations('sam')) == factorial(len('sam'))
        assert len(get_permutations('test')) == factorial(len('test'))
        assert len(get_permutations('longer')) == factorial(len('longer'))

    def test_is_palindrome_permutation(self):
        assert is_palindrome_permutation('hello') is False
        assert is_palindrome_permutation('sam') is False
        assert is_palindrome_permutation('coding') is False

        assert is_palindrome_permutation('nono') is True
        assert is_palindrome_permutation('Tact Coa') is True
        assert is_palindrome_permutation('kayak') is True


if __name__ == '__main__':
    unittest.main()
