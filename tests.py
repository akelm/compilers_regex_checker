import unittest
import re
from parameterized import parameterized

from check_string import check_string

pattern = re.compile(r'^(aa|bb)a(b)*(a)?$')

class TestParser(unittest.TestCase):

    @parameterized.expand([
        '123',
        'ala ma kota',
        'i psa\n',
        'bbb',
        'aaa',
        'aab',
        'aabaaa',
        'aaa',
        'bba',
        'bbbaaaa',
        'bbbaaaab',
        'bbbb',
        'bbbba',
        'abbb',
        'bbbababab',
        'a',
        'babb',
        'b',
        'bbbbbbb'
    ])
    def test_correctness(self, text: str):
        result = 'A' if re.match(pattern, text) else 'N'
        self.assertEqual(result, check_string(text), "text: %s " % text)
