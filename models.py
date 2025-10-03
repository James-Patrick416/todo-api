from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost/todo_api')
Base = declarative_base()

class Task(Base):
    __tablename__= 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
# this creates the table in the database 
Base.metadata.create_all(engine)
print("Tasks table created successfully!")    