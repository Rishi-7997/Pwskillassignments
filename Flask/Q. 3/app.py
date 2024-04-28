from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("name.html")

@app.route("/<name>")
def greet(name):
  return render_template("name.html", username=name)

if __name__ == "__main__":
  app.run(debug=True)
