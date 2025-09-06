from stats import get_book_text, count_words, count_char, sort_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)

    word_count = count_words(text)
    char_counts = count_char(text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
