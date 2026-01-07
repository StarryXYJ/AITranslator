# AI Translator

A simple, full-stack application designed to translate Chinese text into English and extract key vocabulary.

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: Flutter (cross-platform)
- **AI**: Google Gemini API

## Setup

### Backend

1.  Navigate to `src/backend`.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Copy `.env.example` to `.env` and add your `GEMINI_API_KEY`.
4.  Run the server: `uvicorn main:app --reload`.

### Frontend

1.  Navigate to `src/frontend`.
2.  Install dependencies: `flutter pub get`.
3.  Run the app:
    - For desktop: `flutter run -d windows` (or `macos`, `linux`)
    - For web: `flutter run -d chrome`
    - For mobile: Connect your device and run `flutter run`

## Usage

1.  Start the backend server (default: `http://localhost:8000`).
2.  Launch the Flutter app.
3.  Enter Chinese text in the input field.
4.  Click "翻译" (Translate) button.
5.  View the English translation and extracted keywords.
