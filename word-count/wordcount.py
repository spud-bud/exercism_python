def word_count(words):
    import re
    words = words.lower()
    word_dict = {}
    word_list = list(filter(None, re.split('\W+|_', words)))
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


word_count('до🖖свидания!')
