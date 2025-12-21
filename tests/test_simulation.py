from Library import Library
from book_class import Book
from simul_functions import add_book
from simul_functions import remove_book
from simul_functions import new_index
from simul_functions import unexisting_book
import unittest
class Test_library(unittest.TestCase):
   def test_simulation_add(self):
      library = Library()
      len1 = library.__len__()
      add_book(library)
      len2 = library.__len__()
      self.assertEqual(len2 - len1, 1)


   def test_simulation_remove(self):
      library = Library()
      book1 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library.add(book1)
      library.add_col(book1)
      len1 = library.__len__()
      remove_book(library)
      len2 = library.__len__()
      self.assertEqual(len1 - len2, 1)

   def test_simulation_remove_empty(self):
      library = Library()
      len1 = library.__len__()
      remove_book(library)
      len2 = library.__len__()
      self.assertEqual(len1, len2)

   def test_index_empty(self):
      library = Library()
      t1 = new_index(library)
      library.index_collection_look()
      self.assertEqual(t1, library.index_collection_look())


   def test_index(self):
      library = Library()
      book1 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library.add(book1)
      library.add_col(book1)
      t1 = new_index(library)
      library.index_collection_look()
      self.assertEqual(t1, library.index_collection_look())

   def test_unexisting_book(self):
      library = Library()
      book1 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library.add(book1)
      library.add_col(book1)
      with self.assertRaises(KeyError):
         unexisting_book(library)
