import pdb
from models.author import Author
from models.book import Book
import repositories.books_repository as books_repository
import repositories.authors_repository as author_repository

author1 = Author("JRR", "Tolkien", "40")
book1 = Book("LOTR", 1940, author1)
book2 = Book("The Two Towers", 1948, author1)

author_repository.save(author1)
books_repository.save(book1)
books_repository.save(book2)