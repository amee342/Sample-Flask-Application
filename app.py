from flask import Flask

"""
Create an instance of Flask class,
which will be our WSGI application.
"""
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask page. This is an amazing web size. "

@app.route("/index")
def index():
    return "Welcome to the index page."


if __name__=="__main__":
    app.run(debug=True)