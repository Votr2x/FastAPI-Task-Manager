from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(title="Task Manager API")

# Include the task routes
app.include_router(tasks.router)