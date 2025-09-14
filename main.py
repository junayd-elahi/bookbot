from stats import *
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_word = count_words(text)
    sort = sort_characters(count_word)

    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in sort:
        if items["char"].isalpha():
            print(f"{items['char']}: {items['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
