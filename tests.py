import unittest

from parameterized import parameterized

from check_string import check_string
from settings import *


class TestParser(unittest.TestCase):

    @parameterized.expand([
        '123',
        'ala ma kota',
        'i psa\n',
        '111',
        '000',
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
    def test_works_as_expected(self, text):
        result = 'A' if re.match(pattern, text) else 'N'
        self.assertEqual(result, check_string(text, states, alphabet), "text: %s " % text)
