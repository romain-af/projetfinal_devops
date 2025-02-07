from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="Task Manager API")

# Modèle de données pour une tâche
class Task(BaseModel):
    id: str = None  # sera généré lors de la création
    title: str
    description: str = ""

# « Base de données » en mémoire pour la démo
tasks_db = {}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return list(tasks_db.values())

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = str(uuid4())
    tasks_db[task.id] = task
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task.id = task_id
    tasks_db[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"detail": "Task deleted"}
