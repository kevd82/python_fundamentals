from flask import Flask, render_template 
app = Flask(__name__)    

@app.route("/")
def check():
    return render_template("index.html", rows=8, columns=8, colorOne="red", colorTwo="black")

@app.route("/<int:columns>")
def checkcol(columns):
    return render_template("index.html", rows=8, columns=columns, colorOne="red", colorTwo="black")

@app.route("/<int:rows>/<int:columns>")
def checkrowcol(rows, columns):
    return render_template("index.html", rows=rows, columns=columns, colorOne="red", colorTwo="black")

@app.route("/<int:rows>/<int:columns>/<string:colorOne>/<string:colorTwo>")
def checkall(rows, columns, colorOne, colorTwo):
    return render_template("index.html", rows=rows, columns=columns, colorOne=colorOne, colorTwo=colorTwo)

    
    
if __name__=="__main__":     
    app.run(debug=True)   