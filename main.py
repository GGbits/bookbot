class Book:
    def __init__(self, path):
        self.path = path
        self.__text = self.__read_book(path)
        self.__word_count = self.__count_words(self.__text)
        self.__letter_count = self.__count_letters(self.__text)

    def __read_book(self, path):
        with open(path) as f:
            file_contents = f.read()
            return file_contents

    def __count_words(self, book_text):
        words = book_text.split()
        return len(words)
    
    def __count_letters(self, book_text):
        book_text = book_text.lower()
        letter_dict = {}
        for c in book_text:
            if c in letter_dict:
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1
        return letter_dict
    
    def get_text(self):
        return self.__text
    
    def get_words(self):
        return self.__word_count
    
    def get_letter_count(self):
        return self.__letter_count


def report(letter_dict):
    print("test:")


def main():
    book = Book("books/frankenstein.txt")
    print(book.get_text())
    print(f"number of words in book: {book.get_words()}")
    print(f"{book.get_letter_count()}")

if __name__ == "__main__":
    main()
