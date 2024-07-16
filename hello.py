from flask import Flask,render_template
from flask import url_for
import os


# __name__ : double underscore variables (dunders)
app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name = name)

@app.route("/gallery/")
def gallery(name=None):
    return render_template('pictures.html', name = name)

@app.route("/projects/")
def projects(name=None):
    return render_template('projets.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)




