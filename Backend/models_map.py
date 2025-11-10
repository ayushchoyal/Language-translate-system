# Maps language pairs (src->tgt) to MarianMT model names.
# Extend this with any additional pairs you need.
MARIAN_MODELS = {
    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",  # English → Hindi
    ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",  # Hindi → English
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",  # English → French
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",  # French → English
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",  # English → German
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",  # German → English
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",  # English → Spanish
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",  # Spanish → English
    ("en", "mr"): "Helsinki-NLP/opus-mt-en-mr",  # English → Marathi
    ("mr", "en"): "Helsinki-NLP/opus-mt-mr-en",  # Marathi → English
    ("en", "gu"): "Helsinki-NLP/opus-mt-en-gu",  # English → Gujarati
    ("gu", "en"): "Helsinki-NLP/opus-mt-gu-en",  # Gujarati → English
    ("en", "ta"): "Helsinki-NLP/opus-mt-en-ta",  # English → Tamil
    ("ta", "en"): "Helsinki-NLP/opus-mt-ta-en",  # Tamil → English
    ("en", "te"): "Helsinki-NLP/opus-mt-en-te",  # English → Telugu
    ("te", "en"): "Helsinki-NLP/opus-mt-te-en",  # Telugu → English
}
