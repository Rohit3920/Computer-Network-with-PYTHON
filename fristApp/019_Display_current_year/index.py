from flask import Flask, render_template, redirect,abort
import logging
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    year = datetime.now().year
    return render_template("index.html", year= year)

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