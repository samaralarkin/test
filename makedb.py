import sqlite3

db = sqlite3.connect('blathr.sqlite')
c = db.cursor()
c.execute("""create table posts (userid varchar(30), text varchar(255), timestamp datetime default current_timestamp)""")
db.commit()
c.execute("""insert into posts values (1, "hello", 1)""")
db.commit()