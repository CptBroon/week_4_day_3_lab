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