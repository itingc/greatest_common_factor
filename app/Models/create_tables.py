import sqlite3


conn = sqlite3.connect('gcf.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE gcf
          (id INTEGER PRIMARY KEY ASC, 
           x INTEGER NOT NULL,
           y INTEGER NOT NULL,
           gcf INTEGER NOT NULL )
          ''')
conn.commit()
conn.close()
