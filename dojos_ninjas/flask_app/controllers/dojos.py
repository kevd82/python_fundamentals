from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo




@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def show_all():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=dojos)

@app.route("/dojo/<int:id>")
def show_one(id):
    data = {
        "id":id
    }
    return render_template("dojo.html", dojo = Dojo.get_one_ninjas(data))


@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    Dojo.add(request.form)
    return redirect('/')