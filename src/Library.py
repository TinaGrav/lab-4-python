from book_class import Book
from book_collection import BookCollection
from IndexCollection import IndexCollection
class Library(BookCollection, IndexCollection):
    def __init__(self):
        BookCollection.__init__(self)
        IndexCollection.__init__(self)

    def book_collection_look(self):
        books_str = "\n".join(f"{book}" for book in (self.collection))
        return f"{books_str}"

    def index_collection_look(self):
        return f"ISBN: {self.isbn_col}\nAuthor: {self.author_col}\nYear: {self.year_col}"

    def search_by_isbn(self, isbn):
        if not self.isbn_col.get(isbn):
            return "No such book found"
        return self.isbn_col.get(isbn)

    def search_by_author(self, author):
        if not self.author_col.get(author):
            return "No such book found"
        return self.author_col.get(author)

    def search_by_year(self, year):
        if not self.year_col.get(year):
            return "No such book found"
        return self.year_col.get(year)


