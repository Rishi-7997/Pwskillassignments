from flask import Flask, render_template, request, redirect, url_for, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import secrets


app = Flask(__name__)
secret_key = secrets.token_hex(16)  # Generate a 32-character (16 bytes) random hex string
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 9/books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def books():
    books = Book.query.all()
    book_list = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'published': book.published,
        'year': book.year,
        'genre': book.genre,
        'description': book.description
    } for book in books]
    return render_template('books.html', books=book_list)

@app.route('/books/<int:book_id>', methods=['GET'])
def return_book(book_id):
    book = Book.query.get_or_404(book_id)
    book_details = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'published': book.published,
        'year': book.year,
        'genre': book.genre,
        'description': book.description
    }
    return render_template('single_book.html', books=book_details)

@app.route('/books', methods=['POST', 'GET'])
def create_book():
    if request.method == 'POST':
        book_id = Book.query.count() + 1
        title = request.form['title']
        author = request.form['author']
        published = request.form['published']
        year = request.form['year']
        genre = request.form['genre']
        description = request.form['description']
        new_book = Book(
            id=book_id,
            title=title,
            author=author,
            published=published,
            year=year,
            genre=genre,
            description=description
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('create_book.html')

@app.route('/books/<int:book_id>', methods=['POST'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.published = request.form['published']
        book.year = request.form['year']
        book.genre = request.form['genre']
        book.description = request.form['description']
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('update_book.html', book=book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if request.method == 'DELETE':
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('deleted_book.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



