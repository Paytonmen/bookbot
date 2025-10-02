# python
import sys
from stats import get_word_count, get_char_count, sorter

def main(path):
    num_words = get_word_count(path)
    num_chars = get_char_count(path)
    sorted_counts = sorter(num_chars)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char, count in sorted_counts.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print('============= END ===============')

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
main(book_path)