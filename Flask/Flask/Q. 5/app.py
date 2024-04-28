from flask import Flask, request, session, redirect, url_for, render_template
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'  # Replace with a strong secret key
app.config['SESSION_TYPE'] = 'filesystem'  # or other session types
Session(app)


@app.route('/login', methods=['GET', 'POST'])
def login():  
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # Store username in session
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/')
def index():
    username = session.get('username')
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
     app.run(debug=True)