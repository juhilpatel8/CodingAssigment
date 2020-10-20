import argparse
import re
import os

'''
Author - Juhil Patel

1. Read input from a file of words;

2. Find the largest word in the file

3. Transpose the letters in the largest word

4. Show the largest word and the largest word transposed 
'''

def read_words_from_input_file(file_path):
    """
    :param file_path: path of the file to use when getting words from the file
    :return: a list of words from the file

    function description - it reads all words from the specified file of specified file path. 
    """
    print('Reading words from file , file path is:',file_path)
    all_words = []
    with open(file_path, 'r') as file:
        for line in file:
            all_words.extend(line.split())
    file.close()

    if not all_words:
        raise Exception("Input File is empty")

    return all_words


def validate_input_word(word):
    """
    :param word: input string to validate
    :return: boolean

    function description -  This function contains the validation of words based on Regex.
    """
    validated = bool(re.match('^[a-zA-Z]+$', word))
    return validated

def find_longest_word(word_list):
    """
    :param word_list: list of words
    :return:the longest valid word in the file.

    function description - it finds the longest word from a list of words
    """
    longestWord = ['']
    max_len= 0
    for word in word_list:
        isValidWord = validate_input_word(word)
        if isValidWord:
            if len(word) > max_len:
                max_len= len(word)
                longestWord = [word]
            # extra check - if there is more than one longest words
            elif len(word) == len(longestWord[0]):
                longestWord.append(word)
        else:
            print(f'{word} Is an invalid word')

    if len(longestWord) > 1:
        raise Exception("This file contains more than one longest words")
    if len(longestWord[0]) == 0:
        raise Exception("No valid words")

    return longestWord[0]


def transpose_input_word(word):
    """
    Takes an input word and transposes it.

    :param word: input string to transpose
    :return: transposed word as a string
    """
    return word[::-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        default='input/positivecases/validInput.txt',
        help='input file must be placed in input DIR')
    args = parser.parse_args()

    wordlist = read_words_from_input_file(args.path)
    longestword = find_longest_word(wordlist)
    print(f'The longest word is: {longestword}')
    transposedword = transpose_input_word(longestword)
    print(f'The longest transposed word is: {transposedword}')


if __name__ == "__main__":
    main()
