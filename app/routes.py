from flask import jsonify, render_template, request
from app import app
from app.forms import manForm

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = manForm()
    return render_template('index.html', form=form)



@app.route("/getdata", methods=["GET", "POST"])
def getdata():
    print(request.form["date"])
    return 'Success'