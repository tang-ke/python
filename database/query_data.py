import sqlite3, sys

conn = sqlite3.connect('user.db')
curs = conn.cursor()

# this code can display chinese normal
conn.text_factory = str

query = 'SELECT * FROM user WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
#print(names)
for row in curs.fetchall():
	#print(row)
	for pair in zip(names, row):
		print('{}: {}'.format(*pair))
