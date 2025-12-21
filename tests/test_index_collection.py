from book_class import Book
from IndexCollection import IndexCollection
import unittest
class Test_index(unittest.TestCase):
   def test_index(self):
      library = IndexCollection()
      self.assertEqual(library, "Нет книг - нет индексов")

   def test_add(self):
      book1 = Book("Вишнёвый сад", "Антоша Чехонте", 1904, "комедия", "893-2-45-741310-0")
      library = IndexCollection()
      library.add(book1)
      self.assertEqual(library, "ISBN: {'893-2-45-741310-0': Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0}\nAuthor: {'Антоша Чехонте': [Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0]}\nYear: {1904: [Book: Вишнёвый сад, author: Антоша Чехонте, year: 1904, genre: комедия, isbn: 893-2-45-741310-0]}")

   def test_add_with_len_isbn(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      self.assertEqual(library.len_isbn(), 3)


   def test_add_with_len_author(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      self.assertEqual(library.len_author(), 2)


   def test_add_with_len_year(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      self.assertEqual(library.len_year(), 3)

   def test_remove_with_len_isbn(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      library.remove(book2)
      self.assertEqual(library.len_isbn(), 2)

   def test_remove_with_len_author(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      library.remove(book3)
      self.assertEqual(library.len_author(), 1)

   def test_remove_unknown_author(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      book3 = Book("Повести Белочкина", "А. С. Пушкин", 1831, "повесть", "209-5-02-593081-0")
      book4 = Book("Повести Белочкина", "А. С. ПушкинS", 1831, "повесть", "209-5-02-593081-0")
      library = IndexCollection()
      library.add(book1)
      library.add(book2)
      library.add(book3)
      with self.assertRaises(KeyError):
         library.remove(book4)

   def test_remove_unknown_isbn(self):
      book1 = Book("Мастер и Маргаритка", "М. А. Булгаков", 1928, "роман в романе", "903-2-78-741310-0")
      book2 = Book("Собачья печёнка", "М. А. Булгаков", 1925, "повесть", "908-2-20-905673-6")
      library = IndexCollection()
      library.add(book1)
      with self.assertRaises(KeyError):
         library.remove(book2)