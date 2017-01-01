import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('drop table user')

cursor.execute('create table user( id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user(id, name) values(\'1\', \'michael\')')

cursor.execute('insert into user(id, name) values(\'2\', \'janne\')')

print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()



conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('select * from user')

values = cursor.fetchall()

for aa in values : 
	print (aa)



cursor.close()
conn.close()