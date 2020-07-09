__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def is_one_away(string1, string2) -> bool:
    """Checks if two strings are just one edit away"""

    # Check lengths
    if abs(len(string1) - len(string2)) > 1:
        return False

    # Check if both strings are already the same
    if string1 == string2:
        return True

    # If the strings are the same length
    if len(string1) == len(string2):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                string = string2[:i] + string1[i] + string2[i+1:]
                return string == string1

    else:
        # Loop through min, don't want index error
        for i in range(min(len(string1), len(string2))):
            if string1[i] != string2[i]:
                if len(string1) < len(string2):
                    string = string1[:i] + string2[i] + string1[i:]
                    return string == string2
                else:
                    string = string2[:i] + string1[i] + string2[i:]
                    return string == string1

        # Means we have had no differences between the two strings except the
        # last character
        return True


class TestIsOneAway(unittest.TestCase):
    def test_is_one_away(self):
        assert is_one_away('pale', 'ple') is True
        assert is_one_away('ple', 'pale') is True

        assert is_one_away('pale', 'pales') is True
        assert is_one_away('pales', 'pale') is True

        assert is_one_away('pale', 'bale') is True
        assert is_one_away('bale', 'pale') is True

        assert is_one_away('ale', 'pale') is True
        assert is_one_away('pale', 'ale') is True

        assert is_one_away('two words', 'two word') is True
        assert is_one_away('two word', 'two words') is True

        assert is_one_away('test', 'bests') is False
        assert is_one_away('bests', 'test') is False

        assert is_one_away('pale', 'bake') is False
        assert is_one_away('bake', 'pale') is False

        assert is_one_away('pale', 'le') is False
        assert is_one_away('le', 'pale') is False


if __name__ == '__main__':
    unittest.main()
