from flask import Flask, render_template
import requests

app = Flask(__name__)


def text_bold(func):
    def wrapper_func():
        return "<b>" + func() + "</b>"

    return wrapper_func


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/guess/<name>')
def guess_controller(name):
    params = {
        "name": name
    }
    response_gender = requests.get("https://api.genderize.io/", params=params)
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    gender = data_gender["gender"]

    response_age = requests.get("https://api.agify.io/", params=params)
    response_age.raise_for_status()
    data_age = response_age.json()
    age = data_age["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
