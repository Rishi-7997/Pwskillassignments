from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          name = request.form['name']
          email = request.form['email']
          phone = request.form['phone']
          return render_template('index.html', sname=name, semail=email, sphone=phone)
     else:
          return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)