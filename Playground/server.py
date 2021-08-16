from flask import Flask, render_template 
app = Flask(__name__)    

@app.route("/play")
def play():
    return render_template("index.html", number=3, color="blue")

@app.route("/play/<int:number>")
def playnum(number):
    return render_template("index.html", number=number, color="blue")

@app.route("/play/<int:number>/<string:color>")
def sayplaynumcolor(number, color):
    return render_template("index.html", number=number, color=color)


@app.route("/<string:url>")
def error(url):
    return f"Sorry, no response at {url}. Please try again"
    
    
if __name__=="__main__":     
    app.run(debug=True)   