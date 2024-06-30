from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to HOME route!!!"

@app.route('/about')
def about():
    return "Welcome to ABOUT route!!!"

if __name__ == "__main__":
    app.run()