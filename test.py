import unittest

from helper import check_scrambled_form, parse_dict_file, slice_str, read_input, get_byte_map, get_dict_maps
from main import scrmabled_strings


class TestCase(unittest.TestCase):

    def test_get_byte_map(self):
        map = get_byte_map('abbz')
        self.assertEqual([x for x in map],
                         [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

        map = get_byte_map('abb+_+z')  # invalid char ignored
        self.assertEqual([x for x in map],
                         [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

        map = get_byte_map('\n')  # non valid char
        self.assertEqual([x for x in map],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        with self.assertRaises(ValueError):  # frequency over 255
            get_byte_map('a' * 256)

    def test_get_dict_maps(self):
        length_grouped_word_maps = get_dict_maps({'axpaj', 'apxaj', 'pjxdn', 'dnrbt', 'abd'})

        self.assertEqual(len(length_grouped_word_maps), 2)
        self.assertTrue(3 in length_grouped_word_maps)
        self.assertTrue(5 in length_grouped_word_maps)
        self.assertEqual(length_grouped_word_maps[3]['abd'], get_byte_map('abd'))

    def test_check_scrambled_form(self):
        result = check_scrambled_form('aapxj', get_byte_map('aapxj'),
                                      'aapxj', get_byte_map('aapxj'))  # equal
        self.assertTrue(result)

        result = check_scrambled_form('axpaj', get_byte_map('axpaj'),
                                      'aapxj', get_byte_map('aapxj'))
        self.assertTrue(result)

        result = check_scrambled_form('axpaj', get_byte_map('axpaj'),  # frequence diff
                                      'aaapxj', get_byte_map('aaapxj'))
        self.assertFalse(result)

        result = check_scrambled_form('aapxj', get_byte_map('aapxj'),  # end with diff
                                      'aapjx', get_byte_map('aapjx'))
        self.assertFalse(result)

        result = check_scrambled_form('abpxj', get_byte_map('abpxj'),  # diff char set
                                      'aapxj', get_byte_map('aapxj'))
        self.assertFalse(result)

        result = check_scrambled_form('\n', get_byte_map('\n'),
                                      '\n', get_byte_map('\n'))  # special case
        self.assertTrue(result)

        with self.assertRaises(Exception):
            check_scrambled_form('', '')  # param validation

        with self.assertRaises(TypeError):
            check_scrambled_form(2, 333)  # param validation

    def test_parse_dict_file(self):
        dict_words = parse_dict_file('dict.txt')
        self.assertEqual(5, len(dict_words))

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
        self.assertTrue('\n' not in line)

    def test_main(self):
        counter = scrmabled_strings('dict.txt', 'input.txt')
        self.assertEqual(counter, 4)
