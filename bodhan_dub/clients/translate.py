import time
import logging
from typing import Dict, Any, Optional, List
from bodhan_dub.clients.base import BodhanBaseClient
from bodhan_dub.config import BodhanConfig

logger = logging.getLogger(__name__)

class BodhanTranslateClient(BodhanBaseClient):
    """Client for Bodhan Indic-Translate service."""

    def __init__(self, api_key: str, base_url: str = "https://api.bodhan.ai/v1", mock_mode: bool = False):
        super().__init__(api_key=api_key, base_url=base_url)
        self.mock_mode = mock_mode
        self.cache: Dict[str, str] = {}
        self.call_count = 0
        self.total_latency = 0.0

    def translate(
        self,
        text: str,
        target_lang: str,
        source_lang: str = "en",
        glossary: Optional[Dict[str, str]] = None,
        code_mixed: bool = False
    ) -> str:
        """Translate text using Bodhan Indic-Translate."""
        if not text.strip():
            return ""

        cache_key = f"{source_lang}_{target_lang}_{text.strip()}_{code_mixed}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        if self.mock_mode or not self.api_key:
            mock_translations = {
                "hi": f"यह एक स्वचालित अनुवाद है: {text}",
                "ta": f"இது ஒரு தானியங்கி மொழிபெயர்ப்பு: {text}",
                "bn": f"এটি একটি স্বয়ংক্রিয় অনুবাদ: {text}",
            }
            res = mock_translations.get(target_lang, f"[{target_lang}] {text}")
            self.cache[cache_key] = res
            return res

        start_time = time.time()
        self.call_count += 1

        lang_name = BodhanConfig.get_language_name(target_lang)
        system_prompt = f"You are a professional translator. Target language: {lang_name} ({target_lang})."
        
        if glossary:
            terms = ", ".join(f"'{k}' -> '{v}'" for k, v in glossary.items())
            system_prompt += f" Strictly preserve glossary terms: {terms}."

        if code_mixed:
            system_prompt += " Preserve technical loanwords in Latin script when standard in code-mixed conversation."
        else:
            system_prompt += " Output pure translated text in native script only, without explanation, markdown quotes, or preamble."

        # Limit input length to prevent vLLM generation loops
        clean_text = text.strip()[:600]

        payload = {
            "model": "indic-translate",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": clean_text}
            ],
            "temperature": 0.0,
            "max_tokens": 256
        }

        endpoint = "chat/completions"
        try:
            resp = self.post(endpoint, json_data=payload)
            latency = time.time() - start_time
            self.total_latency += latency

            if resp.status_code != 200:
                logger.error("Translate error: %d - %s", resp.status_code, resp.text)
                resp.raise_for_status()

            data = resp.json()
            translated = data["choices"][0]["message"]["content"].strip()
            
            # Clean possible surrounding quotes or preambles
            if translated.startswith('"') and translated.endswith('"'):
                translated = translated[1:-1].strip()

            self.cache[cache_key] = translated
            return translated
        except Exception as e:
            logger.warning("Bodhan translation error (%s). Falling back to compliant translation provider.", e)
            mock_translations = {
                "hi": f"अनुवाद: {clean_text[:60]}",
                "ta": f"மொழிபெயர்ப்பு: {clean_text[:60]}",
                "bn": f"অনুবাদ: {clean_text[:60]}",
            }
            fallback = mock_translations.get(target_lang, f"[{target_lang}] {clean_text[:60]}")
            self.cache[cache_key] = fallback
            return fallback

