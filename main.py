def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import character_count
from stats import sort_dict

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_count = character_count(text)
    sorted_dict = sort_dict(char_count)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for dictionary in sorted_dict:
        if not dictionary["char"].isalpha():
            continue
        print (f"{dictionary['char']}: {dictionary['num']}")
    print ("============= END ===============")

main()