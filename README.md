# AI Translator

A simple, full-stack application designed to translate Chinese text into English and extract key vocabulary.

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: Web (HTML, CSS, JavaScript)
- **AI**: Google Gemini API

## Setup

### Backend

1.  Navigate to `src/backend`.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Copy `.env.example` to `.env` and add your `GEMINI_API_KEY`.
4.  Run the server: `uvicorn main:app --reload`.

### Frontend

1.  Open `src/frontend/index.html` in your web browser.
2.  Or serve it with a simple HTTP server:
    ```bash
    cd src/frontend
    python -m http.server 8080
    ```
3.  Visit `http://localhost:8080` in your browser.

## Usage

1.  Start the backend server (default: `http://localhost:8000`).
2.  Open the frontend in your browser.
3.  Enter Chinese text in the input field.
4.  Click "翻译" (Translate) button.
5.  View the English translation and extracted keywords.
