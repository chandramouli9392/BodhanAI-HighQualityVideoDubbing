import os
from pathlib import Path
from typing import Dict, Any, List
from dotenv import load_dotenv

load_dotenv()

class BodhanConfig:
    """System configuration for Bodhan AI Video Dubbing Pipeline."""
    
    BASE_URL: str = os.getenv("BODHAN_API_BASE_URL", "https://api.bodhan.ai/v1")
    TRANSCRIBE_API_KEY: str = os.getenv("BODHAN_TRANSCRIBE_API_KEY", "")
    TRANSLATE_API_KEY: str = os.getenv("BODHAN_TRANSLATE_API_KEY", "")
    SPEAK_API_KEY: str = os.getenv("BODHAN_SPEAK_API_KEY", "")

    DEFAULT_VOICE: str = os.getenv("BODHAN_DEFAULT_VOICE", "Ananya")
    MIN_SPEEDUP: float = float(os.getenv("BODHAN_MIN_SPEEDUP", "0.85"))
    MAX_SPEEDUP: float = float(os.getenv("BODHAN_MAX_SPEEDUP", "1.20"))
    MAX_CONDENSATION_RETRIES: int = int(os.getenv("BODHAN_MAX_CONDENSATION_RETRIES", "2"))
    TARGET_LUFS: float = float(os.getenv("BODHAN_TARGET_LUFS", "-16.0"))
    TIMELINE_TOLERANCE_MS: float = float(os.getenv("BODHAN_TIMELINE_TOLERANCE_MS", "100.0"))
    SEGMENT_ALIGNMENT_TOLERANCE_MS: float = float(os.getenv("BODHAN_SEGMENT_ALIGNMENT_TOLERANCE_MS", "300.0"))

    # Production-tier supported Indic languages (ISO-639-1 / Bodhan identifiers)
    SUPPORTED_LANGUAGES: Dict[str, str] = {
        "hi": "Hindi",
        "ta": "Tamil",
        "bn": "Bengali",
        "te": "Telugu",
        "mr": "Marathi",
        "gu": "Gujarati",
        "kn": "Kannada",
        "ml": "Malayalam",
        "pa": "Punjabi",
        "or": "Odia",
        "as": "Assamese",
        "ur": "Urdu",
        "sa": "Sanskrit",
    }

    @classmethod
    def get_language_name(cls, code: str) -> str:
        return cls.SUPPORTED_LANGUAGES.get(code.lower(), code)

    @classmethod
    def validate_languages(cls, langs: List[str]) -> List[str]:
        cleaned = []
        for l in langs:
            code = l.strip().lower()
            if not code:
                continue
            cleaned.append(code)
        return cleaned

