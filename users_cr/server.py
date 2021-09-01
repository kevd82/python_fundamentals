from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route("/Read(All)")
def index():
    users = User.get_all()
    return render_template("Read(All).html", all_users = users)

@app.route("/Add")
def add():
    return render_template("/Create.html")

@app.route("/Create", methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/Read(All)')

if __name__ == "__main__":
    app.run(debug=True)