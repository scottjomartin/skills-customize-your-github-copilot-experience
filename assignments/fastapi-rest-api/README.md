# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing tasks. Practice defining HTTP routes, validating request data with Pydantic models, and returning appropriate responses with FastAPI.

## 📝 Tasks

### 🛠️ Define the API and Read Tasks

#### Description
Set up the FastAPI application and add endpoints for checking the service and reading task data.

#### Requirements
Completed program should:

- Create a FastAPI application with a descriptive title.
- Define a task model with an integer ID, a title, and a completed status.
- Implement `GET /` to return a short service message.
- Implement `GET /tasks` to return all tasks and `GET /tasks/{task_id}` to return one task.
- Return an HTTP 404 response when the requested task does not exist.

### 🛠️ Create, Update, and Delete Tasks

#### Description
Add endpoints that let a client change the in-memory task list using standard HTTP methods.

#### Requirements
Completed program should:

- Implement `POST /tasks` to create a task and assign it a unique ID.
- Implement `PUT /tasks/{task_id}` to update a task's title and completed status.
- Implement `DELETE /tasks/{task_id}` to remove a task.
- Return an HTTP 404 response when an update or deletion targets a missing task.
- Run the API locally and use the interactive documentation at `/docs` to try each endpoint.

## ▶️ Getting Started

Install FastAPI and Uvicorn:

```bash
python -m pip install fastapi uvicorn
```

Start the development server from this folder:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore and test the API.
