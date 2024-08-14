from flask import Flask

app = Flask(__name__)



def what_is_happen(func):
       def wraber(*strs):
              i=1
              str=""
              for arg in strs:
                str+=f"<h1>Arg({i}):{arg}</h1>"
              str+func()
              return str
              
              
              
       return wraber



@app.route('/')
@what_is_happen
def hello_word():
       return "<h1>Hello world</h1>\
              <p>hello</p>"





if __name__ == '__main__':
       app.run(debug=True)


