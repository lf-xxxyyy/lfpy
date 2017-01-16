from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Index


engine = create_engine("mysql+pymysql://root:123@localhost:3306/test", max_overflow=5)


Base = declarative_base()

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String(32))

	__table_args__ = (
		Index('ix_id_name', 'name'),
		)


## Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#obj = Users(id='123', name='tony')
#session.add(obj)
#session.commit()

ret = session.query(Users).all()
for i in ret : 
	print (i.id, i.name)