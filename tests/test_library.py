from Library import Library
from book_class import Book
import unittest
class Test_library(unittest.TestCase):
   def test_book_collection(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман",
                   "576-5-90-148410-1")
      book2 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = Library()
      library.add_col(book1)
      library.add_col(book2)
      self.assertEqual(library.book_collection_look(),  "\"Жалкая я букашка или супер-ниндзя черепашка?\" - Ф. М. Достаевский, 1866г. роман ISBN: 576-5-90-148410-1\n\"Вишнёвый сад\" - Антоша Чехонте, 1904г. комедия ISBN: 893-2-45-741310-0")

   def test_index_collection(self):
      book1 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = Library()
      library.add(book1)
      self.assertEqual(library.index_collection_look(), "ISBN: {'893-2-45-741310-0': Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0}\nAuthor: {'Антоша Чехонте': [Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0]}\nYear: {1904: [Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0]}")

   def test_search_by_author(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      self.assertEqual(indlibrary.search_by_author("Р. Л. Стивенсон"), "Book: Клуб самоубийц, author: Р. Л. Стивенсон, year: 1878, genre: детектив, isbn: 904-2-79-784524-0")

   def test_search_by_isbn(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      self.assertEqual(indlibrary.search_by_isbn("904-2-79-784524-0"), "Book: Клуб самоубийц, author: Р. Л. Стивенсон, year: 1878, genre: детектив, isbn: 904-2-79-784524-0")

   def test_search_by_year(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      self.assertEqual(indlibrary.search_by_year(1878), "Book: Клуб самоубийц, author: Р. Л. Стивенсон, year: 1878, genre: детектив, isbn: 904-2-79-784524-0")


   def test_search_by_year(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      self.assertEqual(indlibrary.search_by_year(1878), "Book: Клуб самоубийц, author: Р. Л. Стивенсон, year: 1878, genre: детектив, isbn: 904-2-79-784524-0")

   def test_search_unknown(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      self.assertEqual(indlibrary.search_by_year(1900), "No such book found")

   def test_remove_in_index_col(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add(book1)
      indlibrary.add(book2)
      indlibrary.remove(book2)
      self.assertEqual(indlibrary.len_isbn(), 1)

   def test_remove_in_book_col(self):
      book1 = Book("Жалкая я букашка или супер-ниндзя черепашка?", "Ф. М. Достаевский", 1866, "роман", "576-5-90-148410-1")
      book2 = Book("Клуб самоубийц", "Р. Л. Стивенсон", 1878, "детектив", "904-2-79-784524-0")
      indlibrary = Library()
      indlibrary.add_col(book1)
      indlibrary.add_col(book2)
      indlibrary.remove_col(book2)
      self.assertEqual(indlibrary.__len__(), 1)