import os
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['UPLOAD_FOLDER'] = 'c:/Users/RS/OneDrive/Documents/DS/Ineuron Assignment/Flask/Q. 6/static/files'

class MyForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload file")

@app.route("/", methods=['GET', 'POST'])
def file():
    form = MyForm()
    if form.validate_on_submit():
        f = form.file.data
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f.save(file_path)
        return redirect(url_for('uploaded_file', filename=f.filename))
    return render_template('file.html', form=form)

@app.route('/uploaded_file/<filename>')
def uploaded_file(filename): 
    return render_template('uploaded.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)