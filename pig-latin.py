##
# pig_latin.py
# Converts input to pig latin!
# Dago
# 2021-04-09


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


def separate_nonalpha(string):
    """
    Splits a sentence by words and nonalpha characters.
    Spaces included
    """
    temp = ''
    # This way instead of split so that spaces are conserved
    # To avoid ["hi", ",", "you"] -> " ".join() -> "hi , you"
    # Users can ["hi", ",", " ", "you"] -> ''.join() -> "hi, you"
    sentence = list(string)
    processed_sentence = []

    for char in sentence:
        if char.isalpha():
            # Store up
            temp += char
        else:
            processed_sentence.append(temp)
            processed_sentence.append(char)
            temp = ''  # Reset
    else:
        # Just in case the last word doesnt get added by the previous
        # else
        processed_sentence.append(temp)

    # Filter will clear out any empty strings
    return list(filter(None, processed_sentence))


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
    print(translate_sentence(input()))
