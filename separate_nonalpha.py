##
# pig_latin.py
# Converts input to pig latin!
# Dago
# 2021-04-09

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


if __name__ == "__main__":
    print(separate_nonalpha(input("Separate by non-alpha: ")))
