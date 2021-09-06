from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    return render_template("ninja.html", dojo = Dojo.get_all())

@app.route("/create/ninja", methods = ["POST"])
def create_ninja():
    ninja.Ninja.add(request.form)
    return redirect("/")