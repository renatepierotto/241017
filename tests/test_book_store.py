from lib.book_store import BookStore

"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book_store = BookStore(1, "Test title", "Test author name")
    assert book_store.id == 1
    assert book_store.title == "Test title"
    assert book_store.author_name == "Test author name"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book_store = BookStore(1, "Test title", "Test author name")
    assert str(book_store) == "1 - Test title - Test author name"
    # Try commenting out the `__repr__` method in lib/book_store.py
    # And see what happens when you run this test again.

"""
We can compare two identical books
And have them be equal
"""
def test_artists_are_equal():
    book_store1 = BookStore (1, "Test title", "Test author name")
    book_store2 = BookStore (1, "Test title", "Test author name")
    assert book_store1 == book_store2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
