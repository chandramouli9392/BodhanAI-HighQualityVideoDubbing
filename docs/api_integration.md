# Bodhan AI API Integration Guide

This document documents verified endpoints, authentication mechanisms, and request/response contracts for Bodhan AI's hosted infrastructure.

## Base Configuration
- **Base URL**: `https://api.bodhan.ai/v1`
- **Authentication**: HTTP Bearer Token
  ```http
  Authorization: Bearer <API_KEY>
  ```

---

## 1. Bodhan Indic-Transcribe (Speech Recognition)

- **Endpoint**: `POST https://api.bodhan.ai/v1/audio/transcriptions`
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `file`: Audio file binary (WAV, FLAC, OGG, MP3).
  - `model`: `"indic-transcribe"`
  - `language`: Language code (`"en"` for source, `"hi"`, `"ta"`, `"bn"` for back-transcription).
  - `response_format`: `"verbose_json"` or `"json"`.

### Response Schema:
```json
{
  "text": "Welcome to this artificial intelligence demonstration video.",
  "language": "en",
  "duration": 3.5,
  "segments": [
    {
      "id": "0",
      "start": 0.0,
      "end": 3.5,
      "text": "Welcome to this artificial intelligence demonstration video."
    }
  ]
}
```

---

## 2. Bodhan Indic-Translate (Translation)

- **Endpoint**: `POST https://api.bodhan.ai/v1/chat/completions`
- **Content-Type**: `application/json`
- **Model**: `"indic-translate"` (vLLM inference)
- **Parameters**:
  - `messages`: Array of system and user messages.
  - `temperature`: `0.0` for deterministic, accurate translation.

### Request Example:
```json
{
  "model": "indic-translate",
  "messages": [
    {
      "role": "system",
      "content": "You are a professional translator. Target language: Hindi (hi). Strictly preserve glossary terms."
    },
    {
      "role": "user",
      "content": "Hello, welcome to this video about machine learning."
    }
  ],
  "temperature": 0.0
}
```

### Response Example:
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "नमस्ते, मशीन लर्निंग के बारे में इस वीडियो में आपका स्वागत है।"
      }
    }
  ]
}
```

---

## 3. Bodhan Indic-Speak (Speech Synthesis)

- **Endpoint**: `POST https://api.bodhan.ai/v1/audio/speech`
- **Content-Type**: `application/json`
- **Model**: `"indic-speak"`
- **Parameters**:
  - `input`: Spoken text in native Indic script.
  - `voice`: Speaker name (e.g. `"Ananya"`).
  - `instructions`: JSON string containing language code and style (e.g. `'{"lang": "hi", "style": "news"}'`).

### Request Example:
```json
{
  "model": "indic-speak",
  "input": "नमस्ते, मशीन लर्निंग के बारे में इस वीडियो में आपका स्वागत है।",
  "voice": "Ananya",
  "instructions": "{\"lang\": \"hi\", \"style\": \"news\"}"
}
```

### Response:
- Binary audio stream: 16-bit PCM WAV (or MP3 container), 16/24 kHz.

