from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Active CORS pour permettre au frontend d'accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vous pouvez restreindre cela selon vos besoins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Définition du modèle de tâche
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False  # Indique si la tâche est terminée

# "Base de données" en mémoire pour la démo
tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Hello from the backend"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    # Vérifier si l'ID existe déjà (pour la démo)
    if any(existing.id == task.id for existing in tasks):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(index)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
