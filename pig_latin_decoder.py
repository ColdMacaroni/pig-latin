##
# pig-latin-decoder.py
# Description ------------
# Dago
# 2021-04-13

from pig_latin import *


def decode(string):
    """
    Decodes a string of piglatin and returns all possible translations.
    """
    vowels = ("a", "e", "i", "o", "u")

    VOWEL_FALLBACK = "w"

    word = list(string.lower())

    # This one-liner returns false if any character is not alpha
    # all() applies the and operator to the whole map
    if not all(map(lambda char: char.isalpha(), word)):
        return string

    possible_words = []

    # Remove trailing "ay," it is useless
    word = word[:-len("ay")]

    # - Check for vowels
    # This would equal the vowel fallback if they are the same
    last_chars = ''.join(word[-len(VOWEL_FALLBACK):])
    if word[0] in vowels and last_chars == VOWEL_FALLBACK:
        # Without the fallback
        possible_words.append(''.join(word[:-len(VOWEL_FALLBACK)]))

    # - Get the characters after the last vowel
    # Find last vowel
    last_vowel = -1
    for char in range(0, len(word)):
        if word[char] in vowels:
            last_vowel = char

    # Split the word into two sections: After the first vowel and up to
    # the first vowel
    leftover = word[last_vowel+1:]
    base = word[:last_vowel+1]

    # Cycle through left over by getting the last char and then the
    # penultimate to last, etc.
    # 1, +1 because negative indexes start at 1
    for i in range(1, len(leftover)+1):
        start = leftover[-i:]
        end = leftover[:-i]

        possibility = ''.join(start) + ''.join(base) + ''.join(end)
        possible_words.append(possibility)

    if string[0].isupper():
        # Returns with an uppercase first char
        return list(map(lambda word: word.capitalize(), possible_words))
    else:
        # Returns all lowercase
        return possible_words


def decode_pretty(string):
    """
    Decodes a string of pig-latin and returns in a pretty way
    """
    sentence = separate_nonalpha(string)
    new_sentence = []
    for word in sentence:
        decoded_word = decode(word)

        if len(decoded_word) == 1:
            new_sentence.append(''.join(decoded_word))

        else:
            pretty_word = "( " + ' | '.join(decoded_word) + " )"
            new_sentence.append(pretty_word)

    return ''.join(new_sentence)


if __name__ == "__main__":
    # Code
    while True:
        print(decode_pretty(input()))
