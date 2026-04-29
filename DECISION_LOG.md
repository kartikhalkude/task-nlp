# DECISION_LOG.md

## 1. Time Breakdown

I approached this assignment with the goal of building a clean working solution within the given 4–6 hour limit instead of trying to make it overly complex.

Approximate time breakdown:

- Project setup (FastAPI, folder structure, dependencies): 30 minutes  
- Writing models and core API endpoints manually: 1 hour  
- Building task creation, listing, and completion flow: 45 minutes  
- Smart feature selection and OpenRouter integration: 1.5 hours  
- Debugging API issues and fallback handling: 45 minutes  
- Testing using Swagger/Postman: 30 minutes  
- README and Decision Log documentation: 30–40 minutes  

Total time: Around 5 hours

I intentionally kept the project simple and focused on delivering a reliable working solution rather than adding unnecessary complexity.

---

## 2. Where AI Was Used — and Why

I did not use AI from the beginning for the full project. I first wrote the basic API structure myself, including the task model, endpoints, and in-memory task handling.

I used AI mainly where it saved time during debugging and external API integration.

### OpenRouter integration

I first referred to OpenRouter documentation to understand how the API request should be structured and how the chat completion endpoint works.

After implementing it, I faced issues like model errors, rate limits, and response formatting problems. I then used AI to help debug these issues faster and understand what needed to be corrected.

This was useful because external API debugging can consume a lot of time.

### Debugging API errors

AI helped when handling issues such as:

- 404 model not found  
- 429 rate limit exceeded  
- invalid JSON responses from the model  
- markdown-formatted JSON causing parsing errors  

Instead of spending too much time manually checking every issue, AI helped narrow down the likely causes quickly.

### Documentation support

AI also helped improve the structure of README and Decision Log sections, but the final reasoning and explanations were written manually based on my actual implementation decisions.

---

## 3. Where AI Was NOT Used — and Why

I intentionally wrote the main backend logic myself because I wanted full understanding of the system and did not want to depend blindly on generated code.

### Models and API endpoints

I wrote the task models manually using Pydantic and created the FastAPI routes for:

- POST /tasks  
- GET /tasks  
- PATCH /tasks/{id}  

This helped me keep the API simple and made debugging easier later.

### Architecture decisions

I decided myself to use:

- FastAPI instead of Node.js  
- In-memory storage instead of MongoDB or SQLite  
- Natural Language to Task Conversion as the single smart feature  

These decisions were based on the assignment constraints and time limit, not directly from AI suggestions.

### Fallback logic

I added fallback handling manually because I wanted the API to continue working even if the AI provider failed.

This was important since free LLM providers can be unstable, and I wanted reliability over dependency on a single external service.

---

## 4. At Least 2 Bad AI Outputs (Required)

### Bad Output 1 — Wrong OpenRouter model suggestions

AI initially suggested using some free OpenRouter models that either gave repeated rate limit errors or returned:

"No endpoints found"

which meant the model was unavailable or outdated.

This created confusion because the code itself looked correct, but the provider/model combination was the actual issue.

### How I fixed it

I manually tested multiple available models and switched to:

google/gemma-3-4b-it:free

which worked correctly and returned stable responses.

This showed me that AI suggestions for external APIs are not always updated.

---

### Bad Output 2 — Invalid JSON response format

Sometimes the model returned JSON wrapped inside markdown like this:

```json
{
  ...
}