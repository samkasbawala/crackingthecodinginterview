__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest


def is_substring(pattern: str, string: str) -> bool:
    """Method determines if the string 'pattern' is in the string 'string'"""
    return pattern in string


def is_string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    concat = s2 + s2
    return is_substring(s1, concat)


class TestIsStringRotation(unittest.TestCase):
    def test_is_substring(self):
        tests = [('water', 'waterbottle', True),
                 ('sam', 'sammy', True),
                 ('code', 'coding', False),
                 ('test', 'exam', False)]
        for pattern, string, expected in tests:
            assert is_substring(pattern, string) == expected

    def test_is_string_rotation(self):
        tests = [('waterbottle', 'erbottlewat', True),
                 ('sammy', 'mysam', True),
                 ('noon', 'noonoon', False),
                 ('test', 'test', True),
                 ('xy', 'yx', True)]
        for s1, s2, expected in tests:
            assert is_string_rotation(s1, s2) == expected


if __name__ == '__main__':
    unittest.main()
