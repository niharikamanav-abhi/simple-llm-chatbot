# Dockerfile — Step 5
# Builds the Flask chatbot into a container listening on port 80,
# matching the assignment's exact commands:
#   docker build -t simple-llm-chatbot .
#   docker run -p 80:80 simple-llm-chatbot

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inside the container the app listens on 80 (set via PORT env var,
# app.py reads it). Locally with `python app.py` it still defaults to 5000.
ENV PORT=80
EXPOSE 80

# GROQ_API_KEY is NOT baked in here — pass it at runtime, e.g.:
#   docker run -p 80:80 -e GROQ_API_KEY=your_key simple-llm-chatbot
CMD ["python", "app.py"]