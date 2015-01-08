from flask import Flask, render_template, request, redirect
import sqlite3
import datetime
import cgi
import dateutil.parser

app = Flask(__name__)

@app.route('/')
def home():
    db = sqlite3.connect('blathr.sqlite')
    c = db.cursor()
    c.execute("select * from posts order by timestamp desc")
    out = ''
    for post in c.fetchall():
        out += '<p>' + cgi.escape(post[1]) + '</p><hr>'
    db.close()
    return render_template('template.html', posts=out)
    
@app.route('/', methods=['POST'])
def post():
    text = request.form['text']
    db = sqlite3.connect('blathr.sqlite')
    c = db.cursor()
    c.execute("insert into posts (userid, text) values (1, ?)", [text])
    db.commit()
    db.close()
    return redirect('/', code = 302)


if __name__ == "__main__":
    app.debug = True
    app.run()