# Bodhan.AI Video Dubbing Pipeline (Assignment 4)

An intelligent, production-ready, agentic video dubbing pipeline for Indian languages powered by **Bodhan AI** foundational hosted models.

---

## Key Features

- **Mandatory Bodhan AI Integration**:
  - **Speech Recognition**: Bodhan Indic-Transcribe (`/v1/audio/transcriptions`)
  - **Translation**: Bodhan Indic-Translate (`/v1/chat/completions`)
  - **Speech Synthesis**: Bodhan Indic-Speak (`/v1/audio/speech`)
  - **Quality Assurance**: Back-transcription via Bodhan Indic-Transcribe
- **Strict Video Synchrony**:
  - Preserves original video duration within $\pm 100\text{ ms}$.
  - Aligns dubbed segment starts within $\pm 300\text{ ms}$.
  - Pitch-preserving time-stretching bounded within $0.85\times \dots 1.20\times$.
  - Never modifies video playback speed or presentation timestamps.
- **Agentic English-Side Condensation**:
  - Automatically identifies overlong segments.
  - Condenses English source text and re-translates through Bodhan Indic-Translate.
  - Never independently rewrites or transcreates Indian-language text.
- **Automated Quality Verification**:
  - Character Error Rate (CER) calculation via true Levenshtein distance.
  - Unicode NFC normalization for Indic scripts.
  - Audio artifact detection (silence, clipping).
- **Background Audio Preservation**:
  - Sidechain ducking of original background audio (-12 dB).
  - EBU R128 loudness normalization (-16 LUFS $\pm 1$).
- **Structured Outputs**:
  - SRT and WebVTT subtitles.
  - Comprehensive `report.json` tracking latencies, retries, and metrics.

---

## Supported Languages

The pipeline supports all production-tier Indic languages including:
- **Hindi (`hi`)**
- **Tamil (`ta`)**
- **Bengali (`bn`)**
- **Telugu (`te`)**, **Marathi (`mr`)**, **Gujarati (`gu`)**, **Kannada (`kn`)**, **Malayalam (`ml`)**, **Punjabi (`pa`)**, **Odia (`or`)**, **Assamese (`as`)**, **Urdu (`ur`)**, **Sanskrit (`sa`)**

---

## Installation & Setup

### Prerequisites
- Python 3.11 or newer
- FFmpeg and FFprobe (must be on system `PATH`)

### Setup Environment
```bash
# Clone or open workspace
cd "Bodhan AI"

# Install dependencies
pip install -r requirements.txt
```

### Environment Configuration
Copy `.env.example` to `.env` and configure your Bodhan AI API keys:
```env
BODHAN_API_BASE_URL=https://api.bodhan.ai/v1
BODHAN_TRANSCRIBE_API_KEY=sk-cFp65PZw_vUSVY9SeWJdHw
BODHAN_TRANSLATE_API_KEY=sk-LtRidLdU2ZfsjMfSK-BSVA
BODHAN_SPEAK_API_KEY=sk-WAVim6V4SLquHtuvVB_rNw
```

---

## CLI Usage

### Exact Required Command:
```bash
python -m bodhan_dub --input path/to/video.mp4 --langs hi,ta,bn --out ./out
```

### Optional Arguments:
```bash
python -m bodhan_dub \
  --input path/to/video.mp4 \
  --langs hi,ta,bn \
  --out ./out \
  --glossary configs/glossary.example.yaml \
  --voices configs/voices.example.yaml \
  --code-mixed
```

### Hermetic Test / Mock Mode:
Run without consuming live API credits:
```bash
python -m bodhan_dub --input path/to/video.mp4 --langs hi,ta,bn --out ./out --mock
```

---

## Output Structure

```
out/
├── report.json
├── transcript.en.json
├── hi/
│   ├── video.hi.mp4
│   ├── subtitles.hi.srt
│   ├── subtitles.hi.vtt
│   └── segments.hi.json
├── ta/
│   ├── video.ta.mp4
│   ├── subtitles.ta.srt
│   ├── subtitles.ta.vtt
│   └── segments.ta.json
└── bn/
    ├── video.bn.mp4
    ├── subtitles.bn.srt
    ├── subtitles.bn.vtt
    └── segments.bn.json
```

---

## Testing

Run all unit, integration, and acceptance tests:
```bash
python -m pytest tests/
```

---

## Documentation

Detailed architectural and operational documentation is available in `docs/`:
- [System Architecture](docs/architecture.md)
- [Pipeline Workflow](docs/workflow.md)
- [API Integration](docs/api_integration.md)
- [Testing Guide](docs/testing.md)
- [Design Decisions](docs/design_decisions.md)

