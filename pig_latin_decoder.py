##
# pig-latin-decoder.py
# Description ------------
# Dago
# 2021-04-13
from separate_nonalpha import *
from read_english_dictionary import *

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
        return [string]

    # To avoid index out of range errors in non pig latin inputs
    if len(word) > 2:
        # Remove trailing "ay," it is useless
        word = word[:-len("ay")]
    else:
        return string

    possible_words = []
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


def run_against_dict(word):
    """
    Runs word against a dictionary.
    """
    english_dict = load_words()
    return word.lower() in english_dict


def check_words(ls):
    """
    Returns a list of valid words per run_against_dict()
    Returns as is if not valid
    """
    new_list = []
    valid = False
    for word in ls:   
        if run_against_dict(word):
            valid = True
            new_list.append(word)

    # Return as is if no words are valid
    if not valid:
        new_list = ls

    return new_list


def validated_decode(string):
    """
    Decodes a sentence in pig latin and returns only the valid words.
    """
    sentence = decode_sentence(string)
    valid_sentence = []

    # Validate each word
    for word in sentence:
        valid_sentence.append(check_words(word))

    # Return nicely
    new_sentence = []
    for word in valid_sentence:
        if len(word) == 1:
            new_sentence.append(''.join(word))

        else:
            pretty_word = "( " + ' | '.join(word) + " )"
            new_sentence.append(pretty_word)
            
    return ''.join(new_sentence)
    
def decode_sentence(string):
    """
    Runs a list against the decode function
    """
    sentence = separate_nonalpha(string)
    decoded_sentence = list(map(decode, sentence))

    return decoded_sentence


def decode_pretty(string):
    """
    Decodes a string of pig-latin and returns in a pretty way
    """
    sentence = decode_sentence(string)
    new_sentence = []
    for decoded_word in sentence:
        if len(decoded_word) == 1:
            new_sentence.append(''.join(decoded_word))

        else:
            pretty_word = "( " + ' | '.join(decoded_word) + " )"
            new_sentence.append(pretty_word)

    return ''.join(new_sentence)


if __name__ == "__main__":
    # Code
    while True:
        print(decode_pretty(input("Normal Decode: ")))
        print(validated_decode(input("Valid Decode: ")))
