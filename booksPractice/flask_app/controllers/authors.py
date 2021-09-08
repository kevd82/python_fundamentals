from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book




@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def show_all():
    authors = Author.get_all()
    return render_template("authors.html", all_authors=authors)

@app.route("/author/<int:id>")
def show_one(id):
    data = {
        "id":id
    }
    return render_template("author.html", author = Author.show_book(data))


@app.route("/create/author", methods=["POST"])
def create_author():
    Author.add(request.form)
    return redirect('/')

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")