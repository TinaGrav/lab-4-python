import random
from Library import Library
from book_class import Book

def create_book(book):
    parts = book.split(",")
    isbn = parts[-1]
    genre = parts[-2]
    year = parts[-3]
    author = parts[-4]
    name = ",".join(parts[0:-4])
    return name, author, year, genre, isbn

def add_book(library):
    with open("book_list.txt", "r", encoding='utf-8') as file:
        lines = file.read().splitlines()
        random_line = random.choice(lines)
        name, author, year, genre, isbn = create_book(random_line)
        book1 = Book(name, author, year, genre, isbn)
        library.add(book1)
        library.add_col(book1)
        print(f"New book added: {book1}")


def remove_book(library):
    books = library.collection
    if not books:
        print("No books to remove")
        return
    random_book = random.choice(books)
    library.remove(random_book)
    library.remove_col(random_book)
    print(f"random book removed: {random_book}")


def search_book(library):
    with open("author_list.txt", "r", encoding='utf-8') as file:
        lines = file.read().splitlines()
        random_author = random.choice(lines)
        print(random_author)
        library.search_by_author(random_author)
        answ = library.search_by_author(random_author)
        if answ != "No such book found":
            print("Found:", answ)
        else:
            print(answ)

def new_index(library):
    print("Indexex are already updated: ")
    print(library.index_collection_look())
    return library.index_collection_look()

def unexisting_book(library):
    print("You are trying to get unexsisting book...")
    print("If KeyError was raised, everything went succesfully")
    un_book = Book("Маленький принц", "А. Экзюпери", 1943, "философская сказка", "180-2-39-991310-0")
    library.remove(un_book)

