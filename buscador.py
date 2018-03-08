from flask import Flask
from flask import render_template
from flask import request
import json
import string
from dbhelper import DBHelper

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    data = DB.get_data()
    return render_template("tables_dynamic.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)


