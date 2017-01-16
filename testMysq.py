import mysql.connector
conn = mysql.connector.connect(user='root', password='123', database='test')
cursor = conn.cursor()

cursor.execute('create table useru (id varchar(20))')

cursor.execute('insert into useru (id) values(10)')

conn.commit()
cursor.close()