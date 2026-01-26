from flask import Flask, render_template, redirect, request
import pandas as pd

app = Flask(__name__)

class task:
    def __init__(self,name,description,due_date,date_added,status=False):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status
        self.date_added = date_added
        
        



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")    


if __name__ == "__main__":
    app.run(debug=True)