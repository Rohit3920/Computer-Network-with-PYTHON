from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/<param>')
def about(param):
    return render_template("about.html", name = param)

if __name__ == "__main__":
    app.run(debug=True)