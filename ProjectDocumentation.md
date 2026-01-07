# AI Translator Project Documentation

## 1. Project Overview
The **AI Translator** is a simple, full-stack application designed to translate Chinese text into English and extract key vocabulary. It consists of a Python-based backend powered by the Gemini API and a cross-platform Flutter frontend.

## 2. Technology Stack

### Backend
- **Language**: Python
- **Framework**: FastAPI
- **AI Model**: Google Gemini API
- **Configuration**: `python-dotenv` for environment variable management

### Frontend
- **Framework**: Flutter (Dart)
- **Platforms**: Mobile (iOS/Android), Web, Desktop

## 3. Project Structure
The project follows a standard monorepo structure:

```
AITranslator/
├── .env                # Environment variables (API Keys, etc.)
├── Requirement.md      # Initial requirements
├── ProjectDocumentation.md # This file
└── src/
    ├── backend/        # Backend source code
    │   ├── main.py     # FastAPI entry point
    │   └── requirements.txt # Python dependencies
    └── frontend/       # Flutter source code
        ├── lib/
        │   └── main.dart # Main Flutter application
        └── pubspec.yaml # Flutter dependencies
```

## 4. Backend Specification

### 4.1 Setup
- **Dependency Management**: `pip`
- **Environment Variables**: Store sensitive data in a `.env` file in the backend root.
  ```env
  GEMINI_API_KEY=your_api_key_here
  ```

### 4.2 API Endpoints

#### `POST /translate`
Translates the input Chinese text to English and extracts keywords.

**Request Body (JSON):**
```json
{
  "text": "要翻译的中文内容"
}
```

**Response Body (JSON):**
```json
{
  "translation": "English translation result",
  "keywords": ["Keyword1", "Keyword2", "Keyword3"]
}
```

### 4.3 Logic Flow
1.  Receive `text` from the request.
2.  Construct a prompt for the Gemini API: "Translate the following Chinese text to English and list 3 key vocabulary words from it. Return JSON format."
3.  Parse the Gemini response.
4.  Return the structured JSON to the client.

## 5. Frontend Specification

### 5.1 UI Design
The user interface is minimalistic and functional:
1.  **Input Area**: A text field for users to enter Chinese text.
2.  **Action**: A "Translate" button to trigger the API call.
3.  **Result Area**:
    - **Translation**: Text widget displaying the English translation.
    - **Keywords**: A list or chip view displaying the extracted keywords.

### 5.2 Interaction Flow
1.  User enters text and clicks "Translate".
2.  Frontend sends a `POST` request to `http://localhost:8000/translate`.
3.  Show a loading indicator while waiting.
4.  On success: Update UI with translation and keywords.
5.  On failure: Show an error message.

## 6. Implementation Plan

### Phase 1: Backend Development
1.  Initialize `src/backend`.
2.  Install `fastapi`, `uvicorn`, `google-generativeai`, `python-dotenv`.
3.  Implement `POST /translate` logic.
4.  Test with Swagger UI (`/docs`).

### Phase 2: Frontend Development
1.  Build the UI layout.
2.  Integrate HTTP client (`http` package) to connect with the backend.
3.  Handle state (loading, success, error).

### Phase 3: Integration & Testing
1.  Run backend server.
2.  Run Flutter app.
3.  Verify end-to-end translation flow.

### Phase 4: Documentation
1.  Modify .gitignore to verify the security of this open-source project
2.  Write readme.md to illustrate how to build, run and deploy
