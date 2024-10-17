from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository

from lib.book_store_repository import Book_Store_Repository ##NEW

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

connection.seed("seeds/book_store2.sql") ##NEW


# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# Retrieve all books ##NEW
book_store = Book_Store_Repository(connection)
books = book_store.all()

# List them out
# for artist in artists:
#     print(artist)

# List them out ##NEW
for book in books:
    print(book)
