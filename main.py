from fastapi import FastAPI, HTTPException
from models.task import TaskCreate, Task
from utils.parse_task import parse_natural_language_task

app = FastAPI(title="Smart Task Manager API")

# In-memory storage
tasks = []
task_id_counter = 1


@app.get("/")
def home():
    return {
        "message": "Smart Task Manager API is running"
    }


@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_id_counter

    # If nlp is provided
    if task.input:
        parsed = parse_natural_language_task(task.input)

        title = parsed.get("title", "Untitled Task")
        description = parsed.get("description", "")
        status = parsed.get("status", "pending")

    # Structured input
    else:
        if not task.title:
            raise HTTPException(
                status_code=400,
                detail="Title is required if input is not provided"
            )

        title = task.title
        description = task.description or ""
        status = "pending"

    new_task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "status": status
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task


@app.get("/tasks")
def get_tasks():
    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }


@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            return {
                "message": "Task marked as completed",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )