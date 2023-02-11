#imports
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

#Book class and a table
class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    publisher=db.Column(db.String(50),nullable=False)
    publishyear=db.Column(db.String(4),nullable=False)

    def __repr__(self):
        return f"{self.id},{self.name},{self.author},{self.publisher},{self.publishyear}"

#api root
@app.route('/')
def index():
    return 'Book APIs'

#get all books
@app.route('/books')
def get_books():
    books=Book.query.all()
    output=[]
    for book in books:
        book_data={'id':book.id,'name':book.name,'author':book.author,'publisher':book.publisher,'publishyear':book.publishyear}
        output.append(book_data)
    return {"books":output}

#get a book by id
@app.route('/books/<id>')
def get_book(id):
    book=Book.query.get_or_404(id)
    return ({'id':book.id,'name':book.name,'author':book.author,'publisher':book.publisher,'publishyear':book.publishyear})

#add a book
@app.route('/books',methods=['POST'])
def add_book():
   book=Book(name=request.json['name'],author=request.json['author'],publisher=request.json['publisher'],publishyear=request.json['publishyear'])
   db.session.add(book)
   db.session.commit()
   return {'id':book.id}

#delete a book by id
@app.route('/books/<id>',methods=['DELETE'])
def delete_book(id):
    book=Book.query.get(id)
    if book is None:
        return {'error':'Book not found'}
    db.session.delete(book)
    db.session.commit()
    return {'Message':'Book id: ' + id + ' deleted Successfully'}