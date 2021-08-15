from flask import Flask  
app = Flask(__name__)    

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say(name):
    return f"Hi {name}"

@app.route("/repeat/<int:number>/<string:word>")
def repeat(number, word):
    return f"{word * number}"

@app.route("/<string:url>")
def error(url):
    return f"Sorry, no response at {url}. Please try again"
    
    
if __name__=="__main__":     
    app.run(debug=True)   
