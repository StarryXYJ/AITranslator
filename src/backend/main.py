from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("Warning: GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    translation: str
    keywords: list[str]

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        prompt = f"""
        Translate the following Chinese text to English and list 3 key vocabulary words from it.
        Return the result in the following JSON format:
        {{
            "translation": "English translation result",
            "keywords": ["Keyword1", "Keyword2", "Keyword3"]
        }}

        Text: {request.text}
        """

        response = model.generate_content(prompt)
        
        # Clean up the response text to ensure it's valid JSON
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:-3]
        elif response_text.startswith("```"):
             response_text = response_text[3:-3]

        result = json.loads(response_text)
        
        return TranslationResponse(
            translation=result.get("translation", ""),
            keywords=result.get("keywords", [])
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
