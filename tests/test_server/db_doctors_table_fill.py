import sqlite3
conn = sqlite3.connect('db/test_server.db')

from faker import Faker
fake = Faker()

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS doctors')
c.execute('''CREATE TABLE IF NOT EXISTS doctors
					(name text, birthday text, info text)''')
for _ in range(100):
	name = fake.name()
	date = fake.date(pattern="%Y-%m-%d")
	information = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)

	c.execute('''INSERT INTO doctors(name, birthday, info) VALUES
					(?, ?, ?)''', [name, date, information])

conn.commit()

conn.close()

