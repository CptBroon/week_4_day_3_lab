from db.run_sql import run_sql
from models.book import Book

def select_all():
    books = []
    
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    
    for row in results:
        book = Book(row['title'], row['release_year'], row['author_id'], row["id"])
        books.append(book)
    return books

def save(book):
    sql = "INSERT INTO books (title, release_year, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.release_year, book.author.id]
    
    results = run_sql(sql, values)
    book.id = results[0]['id']
    return book
