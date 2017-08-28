import sys
import sqlite3
conn = sqlite3.connect('db/test_server.db')

c = conn.cursor()

if len(sys.argv) == 1:
	c.execute("DROP TABLE IF EXISTS users")
	c.execute('''CREATE TABLE IF NOT EXISTS users
		(username text, password text)''')
	c.execute('INSERT INTO users values (?, ?)', ["test", "admin"])

	conn.commit()
	conn.close()
elif len(sys.argv) == 2:
	print c.execute("SELECT * FROM users").fetchone()
	conn.close()
else:
	print "I don't know what you're doing"