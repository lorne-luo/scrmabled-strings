import unittest

from helper import check_scrambled_form, parse_dict_file, slice_str, read_input
from main import scrmabled_strings


class TestCase(unittest.TestCase):

    def test_check_scrambled_form(self):
        result = check_scrambled_form('aapxj', 'aapxj')  # equal
        self.assertTrue(result)

        result = check_scrambled_form('axpaj', 'aapxj')
        self.assertTrue(result)

        result = check_scrambled_form('aapxj', 'aapxj')
        self.assertTrue(result)

        result = check_scrambled_form('abpxj', 'aapxj')
        self.assertFalse(result)

        result = check_scrambled_form('\n', '\n')  # special case
        self.assertTrue(result)

        with self.assertRaises(Exception):
            check_scrambled_form('', '')  # param validation

        with self.assertRaises(TypeError):
            check_scrambled_form(2, 333)  # param validation

    def test_parse_dict_file(self):
        dict_words = parse_dict_file('dict.txt')
        self.assertTrue(5 in dict_words)
        self.assertTrue(4, len(dict_words[5]))
        self.assertTrue(3 in dict_words)
        self.assertTrue(4, len(dict_words[3]))

    def test_slice_str(self):
        result = slice_str('aapxjd', 0, 5)
        self.assertEqual(result, 'aapxj')

        result = slice_str('aapxjd', 2, 5)
        self.assertEqual(result, None)

        with self.assertRaises(ValueError):
            slice_str('aapxjd', -1, 5)

        with self.assertRaises(ValueError):
            slice_str('aapxjd', -1, 0)

    def test_read_input(self):
        line = read_input('input.txt')
        self.assertTrue(line.startswith('aa'))

    def test_main(self):
        counter = scrmabled_strings('dict.txt', 'input.txt')
        self.assertEqual(counter, 4)
