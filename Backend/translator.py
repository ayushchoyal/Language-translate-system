from functools import lru_cache
from typing import List
from transformers import MarianTokenizer, MarianMTModel
from models_map import MARIAN_MODELS

class UnsupportedLanguagePair(Exception):
    pass

@lru_cache(maxsize=16)
def load_model(src: str, tgt: str):
    key = (src, tgt)
    if key not in MARIAN_MODELS:
        raise UnsupportedLanguagePair(f"Unsupported language pair: {src}->{tgt}")
    model_name = MARIAN_MODELS[key]
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(texts: List[str], src: str, tgt: str, max_length: int = 512) -> List[str]:
    tokenizer, model = load_model(src, tgt)
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    generated_tokens = model.generate(**inputs, num_beams=4, max_new_tokens=256)
    outputs = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return outputs
