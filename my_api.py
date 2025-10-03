from fastapi import FastAPI
from models import Task
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel

app = FastAPI()
engine = create_engine('postgresql://postgres:postgres@localhost/todo_api')
SessionLocal = sessionmaker(bind=engine)

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return {"tasks": tasks}
class TaskCreate(BaseModel):
    title: str
@app.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()
    new_task = Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()    
    return {"message": "Task created", "task": new_task}