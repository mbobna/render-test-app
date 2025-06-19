import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    text = "We are living in "
    current_year = datetime.datetime.now().year
    return render_template("index.html", text=text, current_year=current_year)

@app.route("/about-me")
def home():
    hobbies = ["cycling", "cooking", "Hiking"]
    return render_template("about.html", hobbies=hobbies)

if __name__ == '__main__':
    app.run(use_reloader=True)