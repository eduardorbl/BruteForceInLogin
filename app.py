from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for flash messages

# Manager of database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                            (username, password)).fetchone()
        conn.close()

        if user:
            return f"Wellcome, {username}! Now bye, there's nothing to see here."
        else:
            flash('You are not in the list, sorry!')
            return redirect(url_for('login'))

    return render_template('login.html')

# Inicializar banco de dados com um usuário
def init_db():
    conn = get_db_connection() # Conect to database
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)') # Create table
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'AS')) # Insert user
    conn.commit() # Commit changes
    conn.close() # Close connection

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(debug=True)
