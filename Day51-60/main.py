from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Girgis To Flask</h1>"

@app.route("about")
def hello_world():
    return "<h1>About page</h1>"


if __name__ == '__main__':
       app.run()