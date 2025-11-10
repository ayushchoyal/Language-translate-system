# Backend Setup


## 1) Create & activate venv (recommended)
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


## 2) Install dependencies
pip install -r requirements.txt
> **Note:** If you see an error like `ImportError: attempted relative import with no known parent package`, change your import in `main.py` from:
> 
> ```python
> from .translator import translate_text, UnsupportedLanguagePair
> ```
> 
> to:
> 
> ```python
> from translator import translate_text, UnsupportedLanguagePair
> ```


## 3) Run the API 
# If you are inside the 'Backend' directory, use:
uvicorn main:app --reload --port 8000




## 4) Test with curl
curl -X POST "http://127.0.0.1:8000/translate" \
-H "Content-Type: application/json" \
-d '{
"source_lang": "en",
"target_lang": "hi",
"texts": ["Hello, how are you?", "This system translates multiple lines at once."]
}'


## Notes
- First run will download the MarianMT model(s) for the language pair you request.
- To add a new pair, just edit `models_map.py` and restart the server.