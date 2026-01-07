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
model = genai.GenerativeModel('gemini-2.5-flash-lite')

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
        prompt = f"""Translate the following Chinese text to English and extract 3 key vocabulary words.
You MUST respond with ONLY valid JSON in this exact format, with no additional text or markdown:
{{"translation": "English translation here", "keywords": ["word1", "word2", "word3"]}}

Chinese text: {request.text}"""

        print(f"Sending request for text: {request.text}")
        response = model.generate_content(prompt)
        
        # Get the response text
        response_text = response.text.strip()
        print(f"Raw response: {response_text}")
        
        # Clean up the response text to ensure it's valid JSON
        # Remove markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
        elif response_text.startswith("```"):
            response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
        
        response_text = response_text.strip()
        print(f"Cleaned response: {response_text}")
        
        # Parse JSON
        result = json.loads(response_text)
        
        # Validate the response has the required fields
        if "translation" not in result or "keywords" not in result:
            raise ValueError("Response missing required fields: translation or keywords")
        
        return TranslationResponse(
            translation=result.get("translation", ""),
            keywords=result.get("keywords", [])
        )

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Failed to parse: {response_text}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to parse AI response as JSON: {str(e)}"
        )
    except Exception as e:
        print(f"Error: {type(e).__name__}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
