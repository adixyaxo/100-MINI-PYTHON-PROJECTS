from flask import Flask, render_template, redirect, request
import pandas as pd
import datetime

app = Flask(__name__)

def get_tasks():
    tasks_list = pd.read_csv("tasks.csv")
    tasks_list = tasks_list.to_dict()
    return tasks_list

tasks_list = get_tasks()
no_tasks = tasks_list['name'].__len__()

class task:
    def __init__(self,name,description,due_date,date_added=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),status=False):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status
        self.date_added = date_added
        
    def append(self):
        tasks_list['name'][no_tasks]=self.name
        tasks_list['description'][no_tasks]=self.description
        tasks_list['due_date'][no_tasks]=self.due_date
        tasks_list['status'][no_tasks]=self.status
        tasks_list['date_added'][no_tasks]=self.date_added

        
        
@app.route("/")
def index():
    global tasks_list
    return render_template("index.html",tasks_list = tasks_list)

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        print()
        task_info = request.form
        name = task_info["name"]
        description = task_info["description"]
        due_date = task_info["due_date"]
        new_task = task(name,description,due_date)
        new_task.append()
        return redirect("/")
    return render_template("index.html")    


if __name__ == "__main__":
    app.run(debug=True)