from flask import Flask, render_template, request, redirect
import sqlite3
import datetime
import dateutil.parser

app = Flask(__name__)

@app.route('/')
def home():
    db = sqlite3.connect('twit.sqlite')
    c = db.cursor()
    c.execute("select * from tweets")
    out = ''
    for tweet in c.fetchall():
        out += '<p>' + tweet[1] + '</p><hr>'
    db.close()
    return render_template('template.html', posts=out)
    
@app.route('/', methods=['POST'])
def post():
    text = request.form['text']
    db = sqlite3.connect('twit.sqlite')
    c = db.cursor()
    c.execute("insert into tweets values (1, ?, 1)", [text])
    db.commit()
    db.close()
    return redirect('/', code = 302)


if __name__ == "__main__":
    app.debug = True
    app.run()