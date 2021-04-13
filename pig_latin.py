##
# pig_latin.py
# Converts input to pig latin!
# Dago
# 2021-04-09
from separate_nonalpha import *


def pig_latin(string):
    """
    Turns word into its pig latin equivalent. Returns string as-is if
    any of the characters is not alpha: [a-z] or [A-Z]
    """

    # For easier processing
    word = list(string.lower())
    new_word = []

    # This one-liner returns false if any character is not alpha
    # all() applies the and operator to the whole map
    if not all(map(lambda char: char.isalpha(), word)):
        return string

    # Used as ending when first char is vowel
    FALLBACK = 'w'

    # Define vowels
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    leftover = []
    ending = []
    FINAL = ['a', 'y']

    if word[0] in VOWELS:
        ending.append(FALLBACK)
        leftover = word.copy()

    else:
        i = 0  # In case anything goes wrong in the for loop
        # Go through each word
        for i in range(0, len(word)):
            # Add to ending if its a consonant
            if word[i] not in VOWELS:
                ending.append(word[i])

            # When the first vowel appears add whats left
            else:
                break
        leftover = word[i:]

    # Put all together
    new_word = leftover + ending + FINAL

    final_word = ''.join(new_word)

    # Uppercase handling
    if string[0].isupper():
        return final_word.capitalize()

    else:
        return final_word.lower()


def translate_sentence(string):
    """
    Runs the pig_latin function for each word of a sentence
    """

    # Separate the non-alpha characters from the alpha characters
    processed_sentence = separate_nonalpha(string)

    new_sentence = []

    for word in processed_sentence:
        # Translate and add to final
        new_sentence.append(pig_latin(word))

    return ''.join(new_sentence)


if __name__ == "__main__":
    # Code
    while True:
        print(translate_sentence(input("To pig latin: ")))
