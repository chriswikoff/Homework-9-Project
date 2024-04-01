import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
    # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        self.assertIn("Dune", test_object.book_list['book_name'].values)

    def test_2_add_book(self):
    # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        test_object.add_book("Dune", 4)
        self.assertEqual(test_object.num_books_read(), 1)

    def test_3_has_read(self):
    # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        self.assertTrue(test_object.has_read("Dune"))

    def test_4_has_read(self):
    # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        self.assertFalse(test_object.has_read("Foundation"))

    def test_5_num_books_read(self):
    # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        test_object.add_book("To Kill a Mockingbird", 4)
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Dune", 4)
        test_object.add_book("To Kill a Mockingbird", 4)
        test_object.add_book("Farenheit 451", 4)
        test_object.add_book("Moby Dick", 3)
        test_object.add_book("Tom Sawyer", 5)
        test_object.add_book("Killer Angels", 5)
        fav_books = test_object.fav_books()
        self.assertEqual(len(fav_books), 5)
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)