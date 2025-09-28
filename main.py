from stats import get_num_words, character_counter
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
print("----------- Word Count ----------")
print(f"Found {get_num_words(book)} total words")

print("--------- Character Count -------")
character_counter(book)

