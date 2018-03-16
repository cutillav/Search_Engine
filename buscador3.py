from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json
import string
from dbhelper1 import DBHelper

app = Flask(__name__)
DB = DBHelper()

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    data = DB.get_data()
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(data)

@app.route("/")
def home():
    return render_template("tables_dynamic3.html")

if __name__ == '__main__':
    app.run(debug=True)


