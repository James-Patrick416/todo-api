from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://todo_api_db_bsxu_user:6OmhOyBbaj6ZSGXj87bTO8CGO72hUHgp@dpg-d3g23ipr0fns73dmven0-a:5432/todo_api_db_bsxu')
Base = declarative_base()

class Task(Base):
    __tablename__= 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
# this creates the table in the database 
Base.metadata.create_all(engine)
print("Tasks table created successfully!")    