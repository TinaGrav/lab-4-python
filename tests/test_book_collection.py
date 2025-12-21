from book_class import Book
from book_collection import BookCollection
import unittest
class Test_book_class(unittest.TestCase):
   def test_book_collection(self):
      library = BookCollection()
      self.assertEqual(library, [])

   def test_get_item(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = BookCollection()
      library.add_col(book1)
      library.add_col(book2)
      self.assertEqual(library.__getitem__(1), "Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0")

   def test_book_add(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = BookCollection()
      library.add_col(book1)
      library.add_col(book2)
      self.assertEqual(library.__str__(), "\"Жалкая я букашка или супер-ниндзя черепашка?\" - Ф. М. Достаевский, 1866г. роман ISBN: 576-5-90-148410-1\n\"Вишнёвый сад\" - Антоша Чехонте, 1904г. комедия ISBN: 893-2-45-741310-0")


   def test_book_add(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = BookCollection()
      library.add_col(book1)
      library.add_col(book2)
      bo = next(library.__iter__())
      self.assertEqual(bo.__repr__(), "Book: Жалкая я букашка или супер-ниндзя черепашка?, author: Ф. М. Достаевский, year: 1866, genre: роман, isbn: 576-5-90-148410-1")

   def test_book_len(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      book3 = Book("Пиццайоло и Маргарита", "М. А. Булгаков", 1928, "роман", "937-2-32-3864950-0")
      library = BookCollection()
      library.add_col(book1)
      library.add_col(book2)
      library.add_col(book3)
      self.assertEqual(library.__len__(), 3)

   def test_book_remove(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      book3 = Book("Пиццайоло и Маргарита", "М. А. Булгаков", 1928, "роман", "937-2-32-3864950-0")
      library = BookCollection()
      library.add_col(book1)
      library.add_col(book2)
      library.add_col(book3)
      library.remove_col(book1)
      self.assertEqual(library.__len__(), 2)
