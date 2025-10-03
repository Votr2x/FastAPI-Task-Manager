from fastapi import APIRouter, HTTPException
from app.schemas import Task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

tasks_db: list[Task] = []

@router.get("/")
def get_tasks():
    return tasks_db

@router.post("/")
def create_task(task: Task):
    tasks_db.append(task)
    return task

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")