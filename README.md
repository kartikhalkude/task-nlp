# Smart Task Manager API

A simple backend API built for the SDE Intern Assignment.

The goal of this project is to create a clean task management API with one AI-powered smart feature while keeping the implementation simple, fast, and practical within the 4–6 hour time limit.

I chose to build the project using FastAPI with in-memory storage and implemented the smart feature using OpenRouter for Natural Language to Task Conversion.

---

# Tech Stack

* Python
* FastAPI
* Pydantic
* OpenRouter API
* In-memory storage
* Swagger UI for testing

---

# Smart Feature Chosen

## Natural Language to Task Conversion

Instead of only accepting structured task input like title and description, the API can also accept a plain English sentence and convert it into structured task fields using AI.

### Example

Input:

```json
{
  "input": "Finish internship assignment tonight and prepare the decision log"
}
```

AI converts it into:

```json
{
  "title": "Finish Internship Assignment and Prepare Decision Log",
  "description": "Complete the internship assignment by tonight and create a comprehensive decision log.",
  "status": "pending"
}
```

This was chosen because it provides a strong AI signal while keeping the backend simple and focused.

---

# Project Structure

```text
smart_task_manager/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── models/
│   └── task.py
│
├── utils/
│   └── parse_task.py
│
├── README.md
└── DECISION_LOG.md
```

---

# How to Start the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/kartikhalkude/task-nlp.git
cd smart_task_manager
```

---

## Step 2: Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Create `.env` File

Create a `.env` file in the root folder and add:

```env
OPENROUTER_API_KEY=your_api_key_here
PORT=8000
```

You can generate a free API key from OpenRouter.

---

## Step 5: Start the FastAPI Server

Run:

```bash
uvicorn main:app --reload
```

You should see output like:

```text
Uvicorn running on http://127.0.0.1:8000
```

This means your project has started successfully.

---

## Step 6: Open Swagger Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

This is the built-in FastAPI testing interface where you can test all API endpoints.

---

# API Endpoints

## POST /tasks

Create a new task.

Supports both:

* structured input
* natural language input

### Structured Input Example

```json
{
  "title": "Submit project report",
  "description": "Before tomorrow evening"
}
```

### Natural Language Input Example

```json
{
  "input": "Finish internship assignment tonight and prepare the decision log"
}
```

---

## GET /tasks

Returns all created tasks.

### Example Response

```json
{
  "total_tasks": 1,
  "tasks": [
    {
      "id": 1,
      "title": "Submit project report",
      "description": "Before tomorrow evening",
      "status": "pending"
    }
  ]
}
```

---

## PATCH /tasks/{id}

Mark a task as completed.

### Example

```text
PATCH /tasks/1
```

### Response

```json
{
  "message": "Task marked as completed",
  "task": {
    "id": 1,
    "title": "Submit project report",
    "description": "Before tomorrow evening",
    "status": "completed"
  }
}
```

---

# Error Handling

Since free OpenRouter models may return:

* rate limit errors
* invalid JSON
* temporary provider failures

fallback logic was added.

If AI parsing fails, the system still creates the task using the raw input instead of breaking the API flow.

This improves reliability and prevents task creation failure.

---

# Assumptions Made

* Persistence durability was not required, so in-memory storage was used
* Authentication and user management were outside assignment scope
* Only one AI-powered smart feature was implemented as required
* Simplicity and working delivery were prioritized over production-level architecture

---

# Future Improvements

Given more time, I would improve:

* SQLite persistence instead of in-memory storage
* Better duplicate task detection
* Improved prompt engineering for more consistent AI output
* Automated unit testing
* Better validation and error handling

---

# Submission Notes

This project was intentionally kept simple and focused.

The goal was to demonstrate:

* execution speed
* practical decision-making
* effective AI usage
* clean backend implementation
* awareness of trade-offs

rather than building unnecessary complexity.
