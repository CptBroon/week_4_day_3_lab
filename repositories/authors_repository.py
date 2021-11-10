from db.run_sql import run_sql
from models.author import Author

def select_all():
    authors = []
    
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['age'], row["id"])
        authors.append(author)
    return authors

def save(author):
    sql = "INSERT INTO authors (first_name, last_name, age) VALUES (%s, %s, %s) RETURNING *"
    values = [author.first_name, author.last_name, author.age]
    
    results = run_sql(sql, values)
    author.id = results[0]['id']
    return author