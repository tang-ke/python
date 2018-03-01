import sqlite3

def convert(value):
	print(value)
	if not value:
		value = '0'
	return str(value)

conn = sqlite3.connect('user.db')
curs = conn.cursor()

# this code can import chinese normal
conn.text_factory = str

curs.execute('''
CREATE TABLE user (

id TEXT PRIMARY KEY,
name	TEXT,
age	TEXT,
gender	TEXT,
IDcode	TEXT
)
''')

query = 'INSERT INTO user VALUES (?,?,?,?,?)'
field_count = 5
for line in open('user.txt'):
	fields = line.split(' ')
	print(fields)
	vals = [convert(f) for f in fields[:field_count]]
	curs.execute(query, vals)

conn.commit()
conn.close()
