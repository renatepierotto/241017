from lib.book_store_repository import Book_Store_Repository
from lib.book_store import BookStore

"""
When we call Book_Store_Repository#all
We get a list of book objects reflecting the seed data.
"""
def test_get_all_books(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = Book_Store_Repository(db_connection) # Create a new BookStoretRepository

    books = repository.all() # Get all artists

    # Assert on the results
    assert books == [
        BookStore (1,'Nineteen Eighty-Four','George Orwell'),
        BookStore (2,'Mrs Dalloway', 'Virginia Woolf'),
        BookStore (3,'Emma', 'Jane Austen'),
        BookStore (4,'Dracula', 'Bram Stoker'),
        BookStore (5,'The Age of Innocence', 'Edith Wharton')
    ]

"""
When we call Book_Store_Repository#find
We get a single book object reflecting the seed data.
"""
def test_get_single_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = Book_Store_Repository(db_connection)

    book = repository.find(3)
    assert book == BookStore (3,'Emma', 'Jane Austen')

"""
When we call Book_Store_Repository#create
We get a new books in the database.
"""
def test_create_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = Book_Store_Repository(db_connection)

    repository.create(BookStore ("id", "blablabook", "blablaauthor"))

    result = repository.all()
    assert result == [
        BookStore (1,'Nineteen Eighty-Four','George Orwell'),
        BookStore (2,'Mrs Dalloway', 'Virginia Woolf'),
        BookStore (3,'Emma', 'Jane Austen'),
        BookStore (4,'Dracula', 'Bram Stoker'),
        BookStore (5,'The Age of Innocence', 'Edith Wharton'),
        BookStore (6,'blablabook', 'blablaauthor')
    ]

"""
When we call Book_Store_Repository#delete
We remove a record from the database.
"""
def test_delete_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = Book_Store_Repository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        BookStore (1,'Nineteen Eighty-Four','George Orwell'),
        BookStore (2,'Mrs Dalloway', 'Virginia Woolf'),
        BookStore (4,'Dracula', 'Bram Stoker'),
        BookStore (5,'The Age of Innocence', 'Edith Wharton'),
    ]