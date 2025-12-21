from book_class import Book
class IndexCollection():
    def __init__(self):
        self.isbn_col = {}
        self.author_col = {}
        self.year_col = {}

    def add(self, book):
        self.isbn_col[book.isbn] = book
        if book.author not in self.author_col:
            self.author_col[book.author] = []
        self.author_col[book.author].append(book)
        if book.year not in self.year_col:
            self.year_col[book.year] = []
        self.year_col[book.year].append(book)

    def remove(self, book):
        if book.isbn not in self.isbn_col:
            raise KeyError("No such book found")
        else:
            del self.isbn_col[book.isbn]

        if book.author not in self.author_col:
            raise KeyError("No such book found")
        else:
            self.author_col[book.author].remove(book)
            if not self.author_col[book.author]:
                del self.author_col[book.author]

        if book.year not in self.year_col:
            raise KeyError("No such book found")
        else:
            self.year_col[book.year].remove(book)
            if not self.year_col[book.year]:
                del self.year_col[book.year]

    def __repr__(self):
        if not self.isbn_col:
            return f"Нет книг - нет индексов"
        return f"ISBN: {self.isbn_col}\nAuthor: {self.author_col}\nYear: {self.year_col}"
    def len_isbn(self):
        return len(self.isbn_col)
    def len_author(self):
        return len(self.author_col)
    def len_year(self):
        return len(self.year_col)


