from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    data = "Hello this is a variable"
    return render_template("index.html", data= data)

@app.route('/display')
def display():
    return render_template("display.html")

@app.route('/redtrect-to-Hello')
def redirect_to_Hello():
    return redirect('/display')

if __name__ == "__main__":
    app.run(debug=True)