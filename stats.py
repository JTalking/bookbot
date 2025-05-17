def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict