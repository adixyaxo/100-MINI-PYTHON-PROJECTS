from flask import Flask, render_template, redirect, request
import pandas as pd

app = Flask(__name__)

def get_tasks():
    tasks_list = pd.read_csv("tasks.csv")
    tasks_list = tasks_list.to_dict()
    return tasks_list

class task:
    def __init__(self,name,description,due_date,date_added,status=False):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status
        self.date_added = date_added


@app.route("/")
def index():
    return render_template("index.html",tasks_list = get_tasks())

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        task_info = request.form
        name = task_info["name"]
    return render_template("index.html")    


if __name__ == "__main__":
    app.run(debug=True)