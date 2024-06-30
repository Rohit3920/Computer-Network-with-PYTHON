from flask import Flask, render_template, redirect,abort
import logging

app = Flask(__name__)

@app.route('/')
def index():
    data = "Hello this is a variable"
    return render_template("index.html", data= data)

@app.route('/display')
def display():
    app.logger.info('Home page accessed')
    return "Welcome to flask"

@app.route('/redtrect-to-Hello')
def redirect_to_Hello():
    return redirect('/display')

@app.route('/not-existing')
def not_exit():
    abort(404)
    


if __name__ == "__main__":
    app.run(debug=True)