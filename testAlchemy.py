from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3



Base = declarative_base()

class User(Base) :
	__tablename__ = 'user'
	id = Column(String(20), primary_key=True)
	name = Column(String(20))


engine = create_engine('sqlite:///test.db')

DBSession = sessionmaker(bind=engine)


session = DBSession()

new_user = User(id='6', name = 'tony6')

#session.add(new_user)

#session.commit()
session.close()



conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('select * from user')

values = cursor.fetchall()

for aa in values : 
	print (aa)

session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print (user.id)
print (user.name)