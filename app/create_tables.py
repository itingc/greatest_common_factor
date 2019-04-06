import sqlite3


conn = sqlite3.connect('gcf.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE gcf
          (id INTEGER PRIMARY KEY ASC, 
           x INTEGER ,
           y INTEGER ,
           gcf INTEGER )
          ''')
conn.commit()
conn.close()
