from book_class import Book
class BookCollection():

    def __init__(self):
        self.collection = []

    def __getitem__(self, index):
        return self.collection[index]

    def __iter__(self):
        return iter(self.collection)

    def __len__(self):
        return len(self.collection)

    def add_col(self, book):
        self.collection.append(book)

    def remove_col(self, book):
        self.collection.remove(book)

    def __str__(self):
        books_str = "\n".join(f"{book}" for book in (self.collection))
        return f"{books_str}"

    def __repr__(self):
        return f"{self.collection}"




