import sqlite3

db = sqlite3.connect('twit.sqlite')
c = db.cursor()
c.execute("""create table tweets (userid varchar(30), text varchar(255), timestamp varchar(30))""")
db.commit()