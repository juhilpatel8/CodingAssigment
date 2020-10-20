import os
import sys
import unittest
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "..")
sys.path.append(path)

from largestwords.largestwords import *


class TestLargestWords(unittest.TestCase):

    def test_functional(self):
        """
       fn() - main() - Tests the entire main file
        """
        main()

    def test_valid_input_words(self):
        """
        fn() - validate_input_word() - Tests valid input for the word validator
        """
        valid_input = ['abcde', 'ab', 'histring']
        for word in valid_input:
            valid = validate_input_word(word)
            self.assertTrue(valid)

    def test_invalid_input_words(self):
        """
        fn() - validate_input_word() - Tests invalid inputs for the word validation
        """
        invalid_input = ['10', '$&', 'j9#']
        for word in invalid_input:
            invalid_input = validate_input_word(word)
            self.assertFalse(invalid_input)


    def test_valid_input_file(self):
        """
       fn() - read_words_from_input_file() - A basic file with valid words separated by new lines
        """
        wordlist = read_words_from_input_file(file_path='input/positivecases/validInput.txt')
        self.assertEqual(wordlist, ['a', 'ab', 'abc', 'abcd', 'abcde'])

    def test_input_file_with_spaces(self):
        """
       fn() - read_words_from_input_file() - A file with new line and whitespace separating words
        """
        wordlist = read_words_from_input_file(file_path='input/positivecases/file_containing_spaces.txt')
        self.assertEqual(wordlist, ['a', 'b', 'cd', 'cd', 'abcde', 'abc'])

    def test_empty_file_throws_exception(self):
        """
        fn() - read_words_from_input_file() - An empty file will throw an exception
        """
        self.assertRaises(
            Exception,
            read_words_from_input_file, 'input/negativecases/emptyInputFile.txt')

    def test_get_longest_word_order_last(self):
        """
        fn() - find_longest_word() - The function should return the longest word even though order wise it is last input
        """
        wordlist = ['a', 'ab', 'abc', 'abcd', 'abcde']
        longest_word = find_longest_word(wordlist)
        self.assertEqual(longest_word, 'abcde')

    def test_get_longest_word_order_first(self):
        """
       fn() - find_longest_word() - The function should return the longest word even though order wise it is first input
        """
        wordlist = ['abcde', 'a','ab', 'abc', 'abcd']
        longest_word = find_longest_word(wordlist)
        self.assertEqual(longest_word, 'abcde')

    def test_all_invalid_words(self):
        """
      fn() - find_longest_word() - If there are no valid words then an exception is raised
        """
        wordlist = ['1', '&^', 'abcd***']
        self.assertRaises(Exception, find_longest_word, wordlist)

    def test_two_equal_largest_words(self):
        """
        fn() - find_longest_word() - If there are Two longest words then an exception is raised
        """
        wordlist = ['z', 'abcd', 'abcd']
        self.assertRaises(Exception, find_longest_word, wordlist)

    def test_tranpose_input_word(self):
        """
        fn() - transpose_input_word() - transpose the valid input word
        """
        word = 'abcde'
        transposed_word = transpose_input_word(word)
        self.assertEqual(transposed_word, 'edcba')




if __name__ == '__main__':
    unittest.main()
