import datetime

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    text = "We are living in "
    current_year = datetime.datetime.now().year
    return render_template("index.html", text=text, current_year=current_year)


@app.route("/about-me", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        hobbies = ["cycling", "cooking", "Hiking"]
        return render_template("about.html", hobbies=hobbies, user_name=user_name)
    elif request.method == "POST":
        name = request.form.get("contact-name")
        email = request.form.get("contact-email")
        message = request.form.get("contact-message")

        response = make_response(render_template("contact.html"))
        response.set_cookie("user_name", name)

        return response

if __name__ == '__main__':
    app.run(use_reloader=True)