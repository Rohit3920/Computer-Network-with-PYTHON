from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = "Hello this is a variable"
    return render_template("index.html", data= data)

@app.route('/img')
def img():
    return '<img src= "/static/img/pics.jpg" width= 400px>'

if __name__ == "__main__":
    app.run(debug=True)