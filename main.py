from stats import get_num_words, get_num_characters, chars_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    characters = get_num_characters(text)
    sorted_list = chars_dict_to_sorted_list(characters)
    print_report(book_path, words, sorted_list)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()



def print_report(book_path, words, sorted_list):
    
    # print the report header
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {book_path}...\n"
    "----------- Word Count ----------\n"
    f"Found {words} total words\n"
    "--------- Character Count -------")

    # print sorted aplhabetical characters with their counts
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    # print the footer
    print("============= END ===============")



main()