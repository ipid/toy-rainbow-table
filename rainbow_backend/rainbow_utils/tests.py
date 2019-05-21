import unittest

from . import util
from . import fmt
from . import r_func


class Tests(unittest.TestCase):

    def test_util_md5(self):
        self.assertEqual(util.md5('abcdef'), 'e80b5017098950fc58aad83c8c14978e')
        self.assertEqual(util.md5_byte('abcdef'),
                         b'\xe8\x0b\x50\x17\x09\x89\x50\xfc\x58\xaa\xd8\x3c\x8c\x14\x97\x8e')
        self.assertEqual(util.md5(''), 'd41d8cd98f00b204e9800998ecf8427e')

    def test_fmt(self):
        self.assertEqual(fmt.fmt_int_8(0), '00000000')
        self.assertEqual(fmt.fmt_int_8(1234567), '01234567')
        self.assertEqual(fmt.fmt_int_8(12345678), '12345678')
        self.assertEqual(fmt.fmt_int_8(123456789), '123456789')

    def test_r_func(self):
        self.assertEqual(r_func.rainbow_r(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'), 1234567)
        self.assertEqual(r_func.rainbow_r(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09'), 12345678)
        self.assertEqual(r_func.rainbow_r(b'\x0a\x0a\x0b\x0b\x0c\x0c\x0d\x0d'), 112233)
        self.assertEqual(r_func.rainbow_r(b'.\x9e\xc3\x17\xe1\x97\x81\x93X\xfb\xc4:\xfc\xa7\xd87'), 68535197)

    def test_rainbow_iter(self):
        self.assertEqual(
            r_func.rainbow_iter(1234567), 68535197
        )
