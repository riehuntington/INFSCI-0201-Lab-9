import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)

@app.route('/')
def index():
    data = get_db()
    return render_template("index.html", all_data = data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("poems.db")
        cursor = db.cursor()
        cursor.execute("select * from poems")
        all_data = cursor.fetchall()
        all_data = [val for val in all_data]
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()