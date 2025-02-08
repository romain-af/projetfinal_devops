from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

# Middleware CORS pour autoriser les requêtes depuis votre frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, précisez l'origine autorisée (ex: ["http://localhost"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle de données pour une tâche
class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: Optional[date] = None  # Date d'échéance optionnelle
    completed: bool = False

# "Base de données" en mémoire
tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Hello from the backend"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/search", response_model=List[Task])
def search_tasks(query: Optional[str] = Query(None, description="Mot-clé de recherche")):
    if query:
        return [
            task for task in tasks
            if query.lower() in task.title.lower() or query.lower() in task.description.lower()
        ]
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
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

# Modèle pour la suppression multiple
class DeleteTasksRequest(BaseModel):
    ids: List[int]

@app.post("/tasks/delete-many")
def delete_many_tasks(request: DeleteTasksRequest):
    ids = request.ids
    deleted = []
    not_found = []
    # Pour chaque identifiant fourni, tenter de supprimer la tâche correspondante
    for task_id in ids:
        found = False
        # Parcours de la liste des tâches
        for index, t in enumerate(tasks):
            if t.id == task_id:
                tasks.pop(index)
                deleted.append(task_id)
                found = True
                break
        if not found:
            not_found.append(task_id)
    return {"deleted": deleted, "not_found": not_found}
