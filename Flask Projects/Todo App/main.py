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
        global no_tasks
        global tasks_list
        tasks_list['name'][no_tasks]=self.name
        tasks_list['description'][no_tasks]=self.description
        tasks_list['due_date'][no_tasks]=self.due_date
        tasks_list['status'][no_tasks]=self.status
        tasks_list['date_added'][no_tasks]=self.date_added
        no_tasks+=1
        df = pd.DataFrame(tasks_list)
        df.to_csv("tasks.csv",index=False)
    
    @staticmethod
    def delete(index):
        global tasks_list
        global no_tasks
        del tasks_list['name'][index]
        del tasks_list['description'][index]
        del tasks_list['due_date'][index]
        del tasks_list['status'][index]
        del tasks_list['date_added'][index]
        print(tasks_list)
        no_tasks-=1
        df = pd.DataFrame(tasks_list)
        df.to_csv("tasks.csv",index=False)
        
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

@app.route("/delete",methods = ["GET","POST"])
def delete():
    global tasks_list
    global no_tasks
    print("delete action was run")
    if 'index' in request.args.keys():
        index = request.args['index']
        print(index)
        if index!=None:
            task.delete(int(index))
            return redirect("/")
    return render_template("index.html",index=None,tasks_list = tasks_list,no_tasks=no_tasks)
        

if __name__ == "__main__":
    app.run(debug=True)