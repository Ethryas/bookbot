import sys
from stats import count_words, get_book_text, count_characters, sort_characters

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")
    book_text = get_book_text(book)
    print("--------- Word Count ---------")
    count_words(book_text)
    print("--------- Character Count ---------")
    char_list = sort_characters(count_characters(book_text))
    for item in char_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    return

main()