### Building URL dynamically
## Variable Rule
### Jinja 2 Temptlate Engine: take the value as parameter for the template

from flask import Flask, render_template, request

"""
Create an instance of Flask class,
which will be our WSGI application.
"""
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask page</H1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


    
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f"Hope you have a nice day, {name}!"
    else:
        return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)