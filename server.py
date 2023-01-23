from flask import Flask, render_template
import requests

agify_endpoint = "https://api.agify.io"
genderize_endpoint = "https://api.genderize.io?"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/guess/<name>')
def guess(name):
    parameters = {"name": name}
    response_agify = requests.get(agify_endpoint, params=parameters)
    agify_dict = response_agify.json()
    age = agify_dict["age"]
    response_genderize = requests.get(genderize_endpoint, params=parameters)
    genderize_dict = response_genderize.json()
    gender = genderize_dict["gender"]
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
