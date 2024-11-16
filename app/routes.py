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
    print(date)
    city = request.form["city"]
    print(city)
    lat, lon, tz = get_coordinates(city)
    pred, plan = predict(date, lat, lon, tz)
    return jsonify({"predictions": pred, "planets": plan}), 200