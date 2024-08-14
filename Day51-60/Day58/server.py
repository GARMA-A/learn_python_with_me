from flask import Flask , render_template
from datetime import datetime as dt
import requests



app = Flask(__name__)
curyear = str(dt.now()).split("-")[0]


@app.route("/")
def say_hello():     
      return render_template("index.html" , year=curyear)

@app.route("/<name>")
def say_name(name):  
       data = requests.get(f"https://api.agify.io?name={name}")
       agedict =  data.json()['age']   
       return render_template("index.html" ,name=name, age=agedict)


if __name__ == "__main__":
       app.run(debug=True)
