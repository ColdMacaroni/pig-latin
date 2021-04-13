##
# pig-latin-decoder.py
# Description ------------
# Dago
# 2021-04-13

from pig_latin import *


def decoder(string):
    """
    Decodes a string of piglatin and returns all possible translations.
    """
    vowels = ("a", "e", "i", "o", "u")

    VOWEL_FALLBACK = "w"

    word = list(string.lower())

    possible_words = []

    # Remove trailing "ay," it is useless
    word = word[:-len("ay")]

    # - Check for vowels
    # This would equal the vowel fallback if they are the same
    last_chars = ''.join(word[-len(VOWEL_FALLBACK):])
    if word[0] in vowels and last_chars == VOWEL_FALLBACK:
        # Without the fallback
        possible_words.append(word[:-len(VOWEL_FALLBACK)])

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
    print(base, leftover)

    # Cycle through left over by getting the last char and then the
    # penultimate to last, etc.
    # for i in len(): [-i:]
    return possible_words


if __name__ == "__main__":
    # Code
    pass
