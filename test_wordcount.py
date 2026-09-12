import unittest
from wordcount import count_words

class TestWordCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_one_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_two_words(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_multi_space(self):
        self.assertEqual(count_words("hello   world"), 2)

    def test_leading_trailing_space(self):
        self.assertEqual(count_words("   hello world   "), 2)

    def test_punctuation(self):
        self.assertEqual(count_words("hello, world!"), 2)

    def test_newline(self):
        self.assertEqual(count_words("hello\nworld"), 2)

    def test_tab(self):
        self.assertEqual(count_words("hello\tworld"), 2)

    def test_mixed_case(self):
        self.assertEqual(count_words("Hello WORLD"), 2)

    def test_many_words(self):
        self.assertEqual(count_words("a b c d e f"), 6)

if __name__ == '__main__':
    unittest.main()
