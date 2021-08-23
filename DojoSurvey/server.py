from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "iceni revolt"

@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["favorite_language"] = request.form["favorite_language"]
    session["dojo_location"] = request.form["dojo_location"]
    session["comments"] = request.form["comments"]
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)