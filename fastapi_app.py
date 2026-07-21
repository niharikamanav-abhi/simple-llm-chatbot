"""
fastapi_app.py  —  Step 4

A REST API version of the same chatbot — separate from app.py (Flask UI).
Both import the same get_response() from chatbot.py, so behaviour is identical;
this just exposes it as a clean API endpoint instead of a browser page.

How to run this in VS Code:
  1. Make sure Step 3 (app.py) already worked for you.
  2. Open a terminal in this folder and run:
       uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --reload
  3. Open http://127.0.0.1:8000/docs in your browser — this is FastAPI's
     built-in interactive test page (no Postman/curl needed).
  4. Click on "POST /chat" -> "Try it out" -> edit the message field ->
     "Execute". You should see a real reply in the response body below.

To stop it: click into the terminal and press Ctrl+C.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response

app = FastAPI(title="Chatbot API", description="Simple LLM chatbot API endpoint")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {"status": "Chatbot API is running. POST your message to /chat"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = get_response(req.message)
    return ChatResponse(response=reply)
