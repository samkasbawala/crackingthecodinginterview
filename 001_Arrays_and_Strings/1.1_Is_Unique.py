__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def is_unique(string: str, ds: bool = True) -> bool:
    """Function to see if inputted string has all unique characters"""

    # Using set data structure, O(n) runtime
    if ds:
        seen = set()
        for char in string:
            if char in seen:
                return False
            seen.add(char)
        return True

    # Using no additional data structures, O(n^2) runtime
    else:
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                if string[i] == string[j]:
                    return False
        return True


class TestIsUnique(unittest.TestCase):
    def test_is_unique_false(self):
        assert is_unique('sam kasbawala') is False
        assert is_unique('test') is False
        assert is_unique('unique') is False
        assert is_unique('\n\n') is False
        assert is_unique('\\\\') is False

        assert is_unique('sam kasbawala', ds=False) is False
        assert is_unique('test', ds=False) is False
        assert is_unique('unique', ds=False) is False
        assert is_unique('\n\n', ds=False) is False
        assert is_unique('\\\\', ds=False) is False

    def test_is_unique_true(self):
        assert is_unique('sam') is True
        assert is_unique('qwerty') is True
        assert is_unique('\n\tt') is True
        assert is_unique('2 words') is True
        assert is_unique('coding') is True

        assert is_unique('sam', ds=False) is True
        assert is_unique('qwerty', ds=False) is True
        assert is_unique('\n\tt', ds=False) is True
        assert is_unique('2 words', ds=False) is True
        assert is_unique('coding', ds=False) is True


if __name__ == '__main__':
    unittest.main()
