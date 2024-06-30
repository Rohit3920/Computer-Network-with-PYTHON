from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = "Hello this is a variable"
    return render_template("index.html", data= data)

@app.route('/display')
def display():
    name = request.args.get('name', 'world')
    return render_template("index.html", data= name)

if __name__ == "__main__":
    app.run(debug=True)