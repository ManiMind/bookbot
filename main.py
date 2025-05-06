from stats import get_num_words, get_num_characters


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    characters = get_num_characters(text)
    print(f"{words} words found in the document")
    print(characters)



def get_book_text(path):
    with open(path) as f:
        return f.read()






main()