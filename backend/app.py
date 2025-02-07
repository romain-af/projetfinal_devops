from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Ajout du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permettre tous les domaines. Vous pouvez restreindre cela à votre domaine de frontend.
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les headers
)

# Exemple de modèle et de routes
class Task(BaseModel):
    id: int
    title: str
    description: str

tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Hello from the backend"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task
