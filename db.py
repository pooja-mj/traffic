import sqlite3
import datetime
import random

x = datetime.datetime.now()

conn = sqlite3.connect('sqlite.db')

c = conn.cursor()

lp_numb = "ka09724ghsa"
loc_li=['bit','market','krpuram']


loc = random.choice(loc_li)

dt = datetime.datetime.now()
ltme = str(dt.strftime("%X"))
ldat = str(dt.strftime("%x"))


#cursor.execute("INSERT INTO table VALUES var1, var2, var3,") 
# Insert a row of data
c.execute("INSERT INTO lplogs VALUES (?, ?, ?,?)", (lp_numb,loc,ldat,ltme))

#c.execute("INSERT INTO lplogs  VALUES lp_numb,loc,ldat,ltme")

# Save (commit) the changes
conn.commit()

for row in c.execute('SELECT * FROM lplogs'):
    print (row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()