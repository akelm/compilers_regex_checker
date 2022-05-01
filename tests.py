import unittest
import re
from parameterized import parameterized

from check_string import check_string

pattern = re.compile(r'^(11|00)((10*1?)|(01*0?))$')

class TestParser(unittest.TestCase):

    @parameterized.expand([
        '123',
        'ala ma kota',
        'i psa\n',
        '111',
        '000',
        '001',
        '001000',
        '000',
        '110',
        '1110000',
        '11100001',
        '1111',
        '11110',
        '0111',
        '111010101',
        '0',
        '1011',
        '1',
        '1111111'
    ])
    def test_correctness(self, text: str):
        result = 'A' if re.match(pattern, text) else 'N'
        self.assertEqual(result, check_string(text), "text: %s " % text)
