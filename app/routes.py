from flask import jsonify, render_template, request
from app import app
from app.forms import manForm
from app.city import get_coordinates
from app.lol import predict


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = manForm()
    return render_template('index.html', form=form)



@app.route("/date", methods=["GET", "POST"])
def date():
    date = request.form["date"]
    city = request.form["city"]
    lat, lon, tz = get_coordinates(city)
    pred, plan = predict(date, lat, lon, tz)
    return jsonify({"predictions": pred, "planets": plan}), 200


@app.route("/teams", methods=["GET", "POST"])
def teams():
    return jsonify({"teams" : [{"name": "ml-team", "sostav": "1, 2, 3, 4", "prediction":"This team is a unique combination of creative ideas, analytical approach, and strong leadership. Each member plays an important role: one inspires unconventional solutions, another simplifies complex tasks and connects people, while a third motivates the team to achieve its goals with determination and energy. Together, they create an unbeatable synergy, where every opinion is valued, and the differences in approaches only enrich the work. It is important to continue fostering an atmosphere of openness and respect, trust each other's ideas, and remember to celebrate every victory, which will strengthen team spirit and help achieve greater success."}]})