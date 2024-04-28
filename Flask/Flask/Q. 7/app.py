from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
@app.route('/home')
def home():
    conn = sql.connect('c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 7/school.db')
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    return render_template("home.html", data=data)

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        addr = request.form['addr']
        city = request.form['city']
        pin = request.form['pin']

        conn = sql.connect('c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 7/school.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (name, addr, city, pin))
        conn.commit()
        flash('User Added', 'success')
        return redirect(url_for('home'))
    return render_template("user.html")

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    conn = sql.connect('c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 7/school.db')
    if request.method == 'POST':
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id = ?", (id,))
        conn.commit()
        flash('User Removed', 'success')
        return redirect(url_for('home'))
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", (id,))
        data = cur.fetchone()
        return render_template("delete.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)