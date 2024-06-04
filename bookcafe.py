from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database
books = [
    {"name": "Love theoretically", "author": "Ali Hazelwood", "genre": "STEM, romance", "published_on": "June 13, 2023"},
    {"name": "Check & Mate", "author": "Ali Hazelwood", "genre": "Chess, romance", "published_on": "November 7, 2023"},
    {"name": "the Love Hypothesis", "author": "Ali Hazelwood", "genre": "STEM, romance", "published_on": "September 14, 2021"},
    {"name": "Final Offer", "author": "Lauren Asher", "genre": "Second-chance romance", "published_on": "January 23, 2023"},
    {"name": "Fine Print", "author": "Lauren Asher", "genre": "Sweet romance", "published_on": "July 8, 2021"},
    {"name": "Terms and Conditions", "author": "Lauren Asher", "genre": "Office romance", "published_on": "February 24, 2022"},
    {"name": "Rule book", "author": "Sarah Adams", "genre": "Fake dating", "published_on": "April 2, 2024"},
    {"name": "Cheat sheet", "author": "Sarah Adams", "genre": "Sports romance", "published_on": "August 17, 2021"}
]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return redirect(url_for('book'))
    else:
        return 'Invalid credentials. Please try again.'

@app.route('/book')
def book():
    query = request.args.get('query')
    if query:
        filtered_books = [book for book in books if query.lower() in book['name'].lower()]
    else:
        filtered_books = books
    return render_template('book.html', books=filtered_books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "name": request.form['name'],
            "author": request.form['author'],
            "genre": request.form['genre'],
            "published_on": request.form['published_on']
        }
        books.append(new_book)
        return redirect(url_for('book'))
    return render_template('add_book.html')

@app.route('/edit/<string:name>', methods=['GET', 'POST'])
def edit_book(name):
    book = next((book for book in books if book["name"] == name), None)
    if request.method == 'POST':
        book['name'] = request.form['name']
        book['author'] = request.form['author']
        book['genre'] = request.form['genre']
        book['published_on'] = request.form['published_on']
        return redirect(url_for('book'))
    return render_template('edit_book.html', book=book)

@app.route('/delete/<string:name>')
def delete_book(name):
    global books
    books = [book for book in books if book["name"] != name]
    return redirect(url_for('book'))

@app.route('/cafe')
def cafe():
    return render_template('cafe.html')

if __name__ == "__main__":
    app.run(debug=True)