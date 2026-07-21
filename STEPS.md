# How to run this, one step at a time

Do these in order. Don't move to the next step until the current one gives
you the output described.

---

## Step 0: One-time setup

1. Open this folder in VS Code (`File → Open Folder`).
2. Make sure the **Python** and **Jupyter** extensions are installed in
   VS Code (Extensions tab, search for both, install if missing).
3. Open a terminal in VS Code (`Terminal → New Terminal`) and run:
   ```
   pip install -r requirements.txt
   ```
4. Get a free API key from https://console.groq.com
5. Create a new file in this folder called `.env` (copy `.env.example` and
   rename it), and paste your real key in:
   ```
   GROQ_API_KEY=your_real_key_here
   ```

---

## Step 1: Talk to the model directly (no app yet)

Open **`01_explore_chatbot.ipynb`** in VS Code.

- Run each cell top to bottom using Shift+Enter.
- Pick the Python kernel when prompted (should be the same environment
  you just `pip install`-ed into).
- Read the output of each cell before running the next one.

**You'll know this step worked when:** the "Key loaded" cell says `True`,
and the test message cells print real replies from the model (not errors).

Feel free to edit the question text in the later cells and re-run — this
is the place to get a feel for how the model responds before anything
else is built on top of it.

---

## Step 2: Same logic, as a plain script

Open **`chatbot.py`**.

- Click the "Run Python File" ▶ button in the top-right of VS Code
  (or press F5).
- Check the terminal at the bottom.

**You'll know this step worked when:** the terminal prints the test
question and a real reply underneath it.

This file doesn't do anything new — it's the exact same logic from the
notebook, just saved as a `.py` file so the next step can import it.

---

## Step 3: The actual chat app (Flask)

Open **`app.py`**.

- Click ▶ Run (or F5).
- Watch the terminal — it should say something like:
  ```
  Running on http://127.0.0.1:5000
  ```
- Open that address in your browser.
- Type a question in the chat box and press Send.

**You'll know this step worked when:** you see your message appear, then
a real reply from the model appear underneath it in the chat window.

To stop the app: click into the terminal and press `Ctrl+C`.

---

## What's next (later, once you're happy with the app)

Once Steps 1–3 all work and you've tried a handful of different
questions and you're comfortable with how it behaves, we'll move on to:

- Adding the FastAPI endpoint (a second, separate way to reach the same
  chatbot logic, for programmatic/API access)
- Dockerizing it
- Deploying to AWS

We're deliberately not touching any of that yet — no rush.
