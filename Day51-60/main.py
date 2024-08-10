from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home_page():
    return "<h1>Girgis To Flask</h1>"

@app.route("/about")
def About_page():
    return "<h1>About page</h1>"


if __name__ == '__main__':
       app.run()