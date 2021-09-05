from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User



@app.route("/")
def index():
    return redirect("/Read(All)")

@app.route("/Read(All)")
def show_all():
    return render_template("Read(All).html", users=User.get_all())

@app.route("/Read(One)/<int:id>")
def show_one(id):
    data = {
        "id":id
    }
    return render_template("Read(One).html", user=User.get_one(data))

@app.route("/Edit/<int:id>")
def edit(id):
    data ={
        "id":id
    }
    return render_template("Edit.html", user=User.get_one(data))

@app.route("/Update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/Read(All)")

@app.route("/Delete/<int:id>")
def delete(id):
    data ={
        "id":id
        }
    User.delete(data)
    return redirect("/Read(All)")

@app.route("/Add")
def add():
    return render_template("/Create.html")

@app.route("/Create", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect('/Read(All)')