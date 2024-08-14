from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def say_hello():
       return render_template("index.html")

@app.route('/<cardPage>')
def card_page(cardPage):
       return render_template(f"{cardPage}")


if __name__ == '__main__':
       app.run(debug=True)
       