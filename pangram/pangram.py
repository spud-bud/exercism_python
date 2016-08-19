def is_pangram(sentence):
    english = [chr(x) for x in range(97, 123)]
    for letter in english:
        if letter not in sentence.lower():
            return False
    return True
