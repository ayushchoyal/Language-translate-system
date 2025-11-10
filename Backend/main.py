from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

from models_map import MARIAN_MODELS
from translator import translate_text, UnsupportedLanguagePair

app = FastAPI(title="Language Translate System", version="1.0.0")

# Allow local dev frontends; tighten in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslateRequest(BaseModel):
    source_lang: str = Field(..., description="Source language code, e.g., 'en'")
    target_lang: str = Field(..., description="Target language code, e.g., 'hi'")
    texts: List[str] = Field(..., description="List of texts to translate")

class TranslateResponse(BaseModel):
    translations: List[str]

@app.get("/health")
async def health():
    return {"status": "ok", "supported_pairs": [f"{s}->{t}" for (s, t) in MARIAN_MODELS.keys()]}

@app.post("/translate", response_model=TranslateResponse)
async def translate(body: TranslateRequest):
    try:
        translations = translate_text(body.texts, body.source_lang.lower(), body.target_lang.lower())
        return TranslateResponse(translations=translations)
    except UnsupportedLanguagePair as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {e}")

# Run with: uvicorn main:app --reload --port 8000
# Backend/models_map.py