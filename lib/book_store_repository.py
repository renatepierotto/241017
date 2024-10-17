from lib.book_store import BookStore

class Book_Store_Repository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        book_store = []
        for row in rows:
            item = BookStore (row["id"], row["title"], row["author_name"])
            book_store.append(item)
        return book_store

    # Find a single book by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from books WHERE id = %s', [id])
        row = rows[0]
        return BookStore (row["id"], row["title"], row["author_name"])

    # Create a new book
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, book_store):
        self._connection.execute('INSERT INTO books (title, author_name ) VALUES (%s, %s)', [
                                 book_store.title, book_store.author_name])
        return None

    # Delete a book by their author name
    def delete(self, author_name):
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [author_name])
        return None
