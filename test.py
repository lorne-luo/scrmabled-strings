import unittest

from main import check_scrambled_form


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

        result = check_scrambled_form('a', 'a')  # edge case
        self.assertTrue(result)

        result = check_scrambled_form('', '')  # edge case
        self.assertTrue(result)
