
from stats import get_num_words, sort_char_count
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        print(f"============ BOOKBOT ============")
        print("Analyzing book found at:", book_path)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("-------- Character Count -------")
        sorted_chars = sort_char_count(text)
        for char_info in sorted_chars:
            if char_info["char"].isalpha():
                print(f"{char_info['char']}: {char_info['num']}")
        print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()
   
main()