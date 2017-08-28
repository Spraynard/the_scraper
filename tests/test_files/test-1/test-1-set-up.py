import sqlite3

conn = sqlite3.connect('../test_server/db/test_server.db')

c = conn.cursor()

c.execute('SELECT * FROM doctors')

doctors = c.fetchall()

file = open('test-1.csv', 'ab')

for doctor in doctors:
	name = "\"" + doctor[0] + "\"" 
	birthday = "\"" + doctor[1] + "\"" 
	description = "\"" + doctor[2] + "\""
	doctor_string = (',').join([name, birthday, description + "\n"])
	file.write(doctor_string)
