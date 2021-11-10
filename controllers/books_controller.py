from flask import Flask, render_template
from flask import Blueprint
import repositories.books_repository as books_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = books_repository.select_all()
    return render_template("books/index.html", books=books)