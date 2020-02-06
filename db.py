import sqlite3
conn = sqlite3.connect('sqlite.db')

c = conn.cursor()

lp_numb = "ka09724ghsa"
loc=['bit','market','krpuram']
ldat="23-2-49"
ltme="5:23pm"




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