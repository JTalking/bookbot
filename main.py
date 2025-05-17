def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import character_count

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    print (f"{num_words} words found in the document")
    print (character_count(text))

main()