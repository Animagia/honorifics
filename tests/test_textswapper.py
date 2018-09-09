import unittest

from honorifics.textswapper import TextSwapperInMark


class TestSwapperInMark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.swapper = TextSwapperInMark()

    def test_swap(self):
        self.assertEqual('{*}{*}', self.swapper.swap('{*}{*}'), 'empty swap')
        self.assertEqual('{*}B{*A}', self.swapper.swap('{*}A{*B}'), 'swap')
        self.assertEqual('text{*}{*A}text{*}B{*}text', self.swapper.swap('text{*}A{*}text{*}{*B}text'),
                         'swap with surroundings')
