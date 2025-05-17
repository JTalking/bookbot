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

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list