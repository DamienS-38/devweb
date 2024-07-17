from flask import Flask,render_template
from flask import url_for, request
import os
import ollama
import glob

# __name__ : double underscore variables (dunders)
app = Flask(__name__)

@app.route('/')
def index():
    name_python = 'Matteo'
    return render_template('index.html', name_html = name_python)

@app.route("/gallery/")
def gallery():
    url_images = glob.glob('static/images/*.jpg')
    return render_template('pictures.html', urls = url_images)

@app.route("/projects/")
def projects(name=None):
    return render_template('projets.html', name = name)

@app.route("/story/")
def story():
    image_url = request.args.get('image_url')
    histoire = ollama_story(image_url)
    return histoire



def ollama_story(img):
    res = ollama.chat(
        model="llava",
        messages=[
            {
                'role': 'user',
                'content': 'Describe this image:',
                'images': [img]
            }
        ]
    )
    story = ollama.chat(
        model="llama3",
        messages=[
            {
                'role': 'user',
                'content': f'Tell me a dark tale in french (without translation) about the following description : {res}',
            }
        ]
    )
    return story['message']['content']
   
    

if __name__ == "__main__":
    app.run(debug=True)




