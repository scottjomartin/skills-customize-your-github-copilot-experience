from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {
    1: Task(id=1, title="Try the API", completed=False),
}
next_task_id = 2


@app.get("/")
def read_root():
    # TODO: Return a short message describing the API.
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task, or raise HTTPException with status 404.
    pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskInput):
    # TODO: Create a task with next_task_id, store it, and return it.
    # Declare next_task_id global before incrementing it.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Replace the task's title and completed status, or return 404 if missing.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Remove the task and return a confirmation, or return 404 if missing.
    pass
