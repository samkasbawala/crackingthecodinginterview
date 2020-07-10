__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

import unittest
import re


def compress(string):
    """This function compresses the string

    Runs O(n) time since we walk through the string once."""

    # If the length of the string is less than 2
    if len(string) < 2:
        return string

    # Build new string and set prev char
    newstring = ''
    prev = string[0]
    count = 1

    # Loop through the characters in the string
    for char in string[1:]:
        if char != prev:
            newstring += prev + str(count)
            count = 1
            prev = char
        else:
            count += 1
    newstring += prev + str(count)

    # See if there are numbers that aren't 1
    return newstring if re.sub('[^2-9]', '', newstring) else string


class TestCompress(unittest.TestCase):
    def test_compress(self):
        assert compress('aabcccccaaa') == 'a2b1c5a3'
        assert compress('sammy') == 's1a1m2y1'
        assert compress('sam') == 'sam'
        assert compress('abcdefghijk') == 'abcdefghijk'
        assert compress('test') == 'test'
        assert compress('aaaa') == 'a4'
        assert compress('a') == 'a'


if __name__ == '__main__':
    unittest.main()
