from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database (SQLite for now)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super_secret_key"

db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Vulnerable Login Route (SQL Injection Possible)
@app.route('/login', methods=['POST'])
def vulnerable_login():
    username = request.form['username']
    password = request.form['password']

    # VULNERABLE SQL QUERY (Prone to SQL Injection)
    query = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
    result = db.engine.execute(query)

    if result.fetchone():
        return "Login Successful! (Vulnerable)"
    else:
        return "Invalid Credentials!"

# Secure Login Route (Prepared Statements)
@app.route('/secure-login', methods=['POST'])
def secure_login():
    username = request.form['username']
    password = request.form['password']

    # SECURE QUERY USING PARAMETERIZED STATEMENTS
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return "Login Successful! (Secure)"
    else:
        return "Invalid Credentials!"

if __name__ == '__main__':
    app.run(debug=True)
