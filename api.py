from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello World"}


task_router = APIRouter()
task_list = []

@task_router.post("/task")
async def create_task(task: dict) -> dict:
    task_list.append(task)
    return {"message": "Task added successfully"}

app.include_router(task_router)