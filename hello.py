from flask import Flask,render_template

# __name__ : double underscore variables (dunders)
app = Flask(__name__)
@app.route('/')
def hello_world(name=None):
    return render_template('index.html',name=name)

@app.route('/templates')
def hello_campus(name=None):
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
