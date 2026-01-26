from flask import Flask, render_template, redirect
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def news():


if __name__ == "__main__":
    app.run(debug=True)