from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def hello_world():
    today = todays_date()
    return render_template("index.html", the_date = today)
    
@app.route("/about")
def about_me():
    return render_template("about_me.html")
    
def todays_date():
    today = date.today()
    str_date = today.strftime('%B %d %Y')
    return "The day of today is " + str_date + " :)"

@app.route("/second")
def second_page():
    return render_template("second_page.html")