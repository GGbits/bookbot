# Reads a text file and outputs to console

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def word_count(book_text):
    words = book_text.split()
    return len(words)


def main():
    text = read_book("books/frankenstein.txt")
    print(text)
    print(f"number of words in book: {word_count(text)}")

if __name__ == "__main__":
    main()
