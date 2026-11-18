<div align="center">

# 🎬 Bodhan.AI
# Agentic Video Dubbing Pipeline

### 🌏 Breaking Language Barriers with AI-Powered Video Dubbing

**Transform English videos into natural-sounding Indian-language videos with intelligent translation, speech synthesis, and precise audio-video synchronization.**

<br/>

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Agentic%20Pipeline-8A2BE2?style=for-the-badge)
![Bodhan AI](https://img.shields.io/badge/Powered%20By-Bodhan%20AI-00A86B?style=for-the-badge)
![FFmpeg](https://img.shields.io/badge/Media-FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

<br/>

**English → Hindi | Tamil | Bengali | Telugu | 9+ Indian Languages**

<br/>

[✨ Features](#-key-features) •
[🚀 Installation](#-installation) •
[💻 Usage](#-cli-usage) •
[🧪 Testing](#-testing) •
[📚 Documentation](#-documentation)

</div>

---

## 🌟 Project Overview

**Bodhan.AI Video Dubbing Pipeline** is an intelligent, agentic video localization system designed to convert English videos into multiple Indian languages.

The pipeline combines Bodhan AI's hosted foundational models with an intelligent orchestration layer to automate:

- 🎙️ English speech recognition.
- 🌐 Multilingual translation.
- 🗣️ Natural-sounding Indian-language speech generation.
- ⏱️ Automatic audio-video synchronization.
- 🎚️ Background audio preservation and mixing.
- 🧠 Intelligent English-side sentence condensation.
- 🔍 Automated transcription-based quality verification.

Unlike a basic translation-and-dubbing workflow, this system incorporates adaptive segment planning, duration-aware speech generation, automated quality checks, and structured reporting.

### ⚡ The Pipeline at a Glance

```text
              🎥 INPUT ENGLISH VIDEO
                       │
                       ▼
              🎵 AUDIO EXTRACTION
                    FFmpeg
                       │
                       ▼
             🎙️ BODHAN INDIC-TRANSCRIBE
                English Transcription
                       │
                       ▼
                🧠 AGENTIC PLANNER
             Segmentation & Timing Analysis
                       │
                       ▼
              🌐 BODHAN INDIC-TRANSLATE
               Indian Language Translation
                       │
                       ▼
               🗣️ BODHAN INDIC-SPEAK
                Dubbed Audio Generation
                       │
                       ▼
               ⏱️ AUDIO SYNCHRONIZATION
              Duration & Timing Adjustment
                       │
                       ▼
               🔍 AUTOMATED QA VERIFICATION
                 Back-Transcription & CER
                       │
                       ▼
               🎚️ AUDIO MIXING & MUXING
                  FFmpeg Processing
                       │
                       ▼
              🌏 FINAL DUBBED VIDEOS
                 Hindi | Tamil | Bengali
```

---

## ✨ Key Features

### 🤖 1. Mandatory Bodhan AI Integration

The pipeline uses Bodhan AI hosted models for all core speech and language operations.

| Component | Bodhan AI Model | Endpoint |
|---|---|---|
| Speech Recognition | Indic-Transcribe | `/v1/audio/transcriptions` |
| Translation | Indic-Translate | `/v1/chat/completions` |
| Speech Synthesis | Indic-Speak | `/v1/audio/speech` |
| Quality Verification | Indic-Transcribe | `/v1/audio/transcriptions` |

**Core principle:** All speech recognition, target-language translation, and speech synthesis are performed through Bodhan AI hosted APIs.

### ⏱️ 2. Precision Audio-Video Synchronization

Maintains accurate synchronization between the original video and generated dubbed speech.

- Original video duration preserved within **±100 ms**.
- Dubbed segment start-time alignment within **±300 ms**.
- Pitch-preserving audio time stretching.
- Supported playback-rate adjustment between **0.85× and 1.20×**.
- Original video playback speed and presentation timestamps remain unchanged.

### 🧠 3. Agentic English-Side Condensation

An intelligent agent identifies translated segments that exceed their available speech duration.

Its workflow:

1. Detect overlong translated speech.
2. Analyze the corresponding English source segment.
3. Condense the English source while preserving its meaning.
4. Send the revised English text through Bodhan Indic-Translate again.
5. Regenerate speech using Bodhan Indic-Speak.
6. Re-evaluate timing and synchronization.

**Important:** The agent does not independently rewrite or transcreate Indian-language output.

### 🔍 4. Automated Quality Assurance

The pipeline includes automated checks to evaluate generated speech.

- Back-transcription using Bodhan Indic-Transcribe.
- Character Error Rate (CER) calculation.
- True Levenshtein-distance-based error measurement.
- Unicode NFC normalization for Indic scripts.
- Silence detection.
- Audio clipping detection.
- Segment-level timing verification.

### 🎚️ 5. Background Audio Preservation

Preserves the original video's background audio while integrating generated speech.

- Sidechain ducking of original background audio.
- Background audio attenuation of approximately **−12 dB** during dubbing.
- EBU R128 loudness normalization.
- Target loudness: **−16 LUFS ±1**.
- FFmpeg-based audio mixing and final video muxing.

### 📄 6. Structured Outputs & Reporting

Every language produces a complete set of output files:

- Final dubbed MP4 video.
- SRT subtitles.
- WebVTT subtitles.
- Segment-level JSON metadata.
- Pipeline execution report.
- Original English transcript.

The report tracks processing information, including API latency, retries, synchronization measurements, and quality metrics.

---

## 🌏 Supported Languages

The pipeline is designed to support **13 production-tier Indic languages**, subject to the corresponding Bodhan Indic-Speak model availability.

| Language | Language Code |
|---|---|
| 🇮🇳 Hindi | `hi` |
| 🇮🇳 Tamil | `ta` |
| 🇮🇳 Bengali | `bn` |
| 🇮🇳 Telugu | `te` |
| 🇮🇳 Marathi | `mr` |
| 🇮🇳 Gujarati | `gu` |
| 🇮🇳 Kannada | `kn` |
| 🇮🇳 Malayalam | `ml` |
| 🇮🇳 Punjabi | `pa` |
| 🇮🇳 Odia | `or` |
| 🇮🇳 Assamese | `as` |
| 🇮🇳 Urdu | `ur` |
| 🇮🇳 Sanskrit | `sa` |

**Demonstration languages:** Hindi, Tamil, and Bengali.

---

## 🚀 Installation & Setup

### 1. Prerequisites

Ensure the following tools are installed:

- Python 3.11 or newer.
- FFmpeg.
- FFprobe.
- Git.
- Bodhan AI API credentials.

### 2. Clone the Repository

```bash
git clone https://github.com/chandramouli9392/BodhanAI-HighQualityVideoDubbing.git

cd BodhanAI-HighQualityVideoDubbing

git checkout assignment/video-dubbing-chandramouli9392
```

### 3. Install Dependencies

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create your local `.env` file from the example:

**Windows PowerShell**
```powershell
Copy-Item .env.example .env
```

**Linux / macOS**
```bash
cp .env.example .env
```

Configure your Bodhan AI credentials inside `.env`:

```env
BODHAN_API_BASE_URL=https://api.bodhan.ai/v1

BODHAN_TRANSCRIBE_API_KEY=your_transcribe_api_key
BODHAN_TRANSLATE_API_KEY=your_translate_api_key
BODHAN_SPEAK_API_KEY=your_speak_api_key
```

⚠️ **Security Notice:** Never commit `.env` or expose API credentials in GitHub, screenshots, documentation, or public repositories. Use `.env.example` with placeholders when sharing the project.

### 5. Verify FFmpeg Installation

```bash
ffmpeg -version
ffprobe -version
```

---

## 💻 CLI Usage

### 🎯 Standard Execution

The required command for generating Hindi, Tamil, and Bengali dubbed videos:

```bash
python -m bodhan_dub --input path/to/video.mp4 --langs hi,ta,bn --out ./out
```

### ⚙️ Advanced Execution

Configure an optional glossary, voice preferences, and code-mixed processing:

```bash
python -m bodhan_dub \
  --input path/to/video.mp4 \
  --langs hi,ta,bn \
  --out ./out \
  --glossary configs/glossary.example.yaml \
  --voices configs/voices.example.yaml \
  --code-mixed
```

### 🧪 Mock Execution

Run the pipeline in mock mode without consuming live API credits:

```bash
python -m bodhan_dub \
  --input path/to/video.mp4 \
  --langs hi,ta,bn \
  --out ./out \
  --mock
```

> Mock mode is intended for testing and development. It does not replace live Bodhan API validation.

---

## 📂 Output Structure

After successful execution, the pipeline generates the following structure:

```text
out/
│
├── 📊 report.json
├── 📝 transcript.en.json
│
├── 📁 hi/
│   ├── 🎬 video.hi.mp4
│   ├── 📄 subtitles.hi.srt
│   ├── 📄 subtitles.hi.vtt
│   └── 📊 segments.hi.json
│
├── 📁 ta/
│   ├── 🎬 video.ta.mp4
│   ├── 📄 subtitles.ta.srt
│   ├── 📄 subtitles.ta.vtt
│   └── 📊 segments.ta.json
│
└── 📁 bn/
    ├── 🎬 video.bn.mp4
    ├── 📄 subtitles.bn.srt
    ├── 📄 subtitles.bn.vtt
    └── 📊 segments.bn.json
```

### 📌 Output Description

| File | Purpose |
|---|---|
| `video.<lang>.mp4` | Final dubbed video |
| `subtitles.<lang>.srt` | SRT subtitles |
| `subtitles.<lang>.vtt` | WebVTT subtitles |
| `segments.<lang>.json` | Segment-level translation and timing information |
| `report.json` | Execution metrics, latency, retries, and QA information |
| `transcript.en.json` | Original English transcription |

---

## 🧪 Testing

The project includes unit, integration, and acceptance tests.

Run the complete test suite:

```bash
python -m pytest tests/ -v
```

Run unit tests:

```bash
python -m pytest tests/unit/ -v
```

Run integration tests:

```bash
python -m pytest tests/integration/ -v
```

Run acceptance tests:

```bash
python -m pytest tests/acceptance/ -v
```

**Testing focus:**

- API client behavior.
- Audio extraction and processing.
- Translation and speech-generation workflows.
- Segment timing and synchronization.
- Audio duration constraints.
- Subtitle generation.
- CER calculation and quality verification.
- Pipeline orchestration and reporting.

---

## 📚 Documentation

Explore the project documentation for implementation details and technical decisions.

| Documentation | Description |
|---|---|
| [🏗️ System Architecture](docs/architecture.md) | Overall system design and component architecture |
| [🔄 Pipeline Workflow](docs/workflow.md) | End-to-end dubbing workflow |
| [🔌 API Integration](docs/api_integration.md) | Bodhan AI API integration details |
| [🧪 Testing Guide](docs/testing.md) | Testing strategy and execution |
| [🧩 Design Decisions](docs/design_decisions.md) | Technical choices and implementation rationale |

---

## 🏛️ Technical Architecture

The system is organized into modular components to separate API communication, agentic decision-making, media processing, and quality verification.

```text
bodhan_dub/
│
├── clients/
│   ├── base.py
│   ├── transcribe.py
│   ├── translate.py
│   └── speak.py
│
├── core/
│   ├── orchestrator.py
│   ├── video_engine.py
│   ├── audio_sync.py
│   ├── audio_master.py
│   └── subtitle_engine.py
│
├── agent/
│   ├── planner.py
│   ├── condenser.py
│   ├── qa_verifier.py
│   └── cost_tracker.py
│
├── models/
│   ├── segment.py
│   └── report.py
│
├── cli.py
├── config.py
└── __main__.py
```

### Component Responsibilities

| Component | Responsibility |
|---|---|
| Clients | Bodhan API communication |
| Orchestrator | Coordinates the complete pipeline |
| Planner | Segment planning and timing analysis |
| Condenser | English-side condensation |
| Video Engine | Video and audio extraction/muxing |
| Audio Sync | Segment-level timing adjustments |
| Audio Master | Background mixing and loudness normalization |
| Subtitle Engine | SRT and WebVTT generation |
| QA Verifier | Back-transcription and quality checks |
| Cost Tracker | API usage and latency tracking |

---

## 🔐 Reliability & Engineering Considerations

The implementation is designed around the following engineering principles:

- Modular architecture and separation of responsibilities.
- Configurable language and voice settings.
- API retry and backoff handling.
- Controlled concurrent processing.
- Structured execution logging.
- Explicit audio-duration constraints.
- Automated quality verification.
- Reproducible mock-mode testing.
- Environment-based credential management.

---

## 🎯 Project Objectives

The project aims to demonstrate how hosted foundational AI models can be combined with agentic orchestration and traditional media-processing tools to build a practical multilingual video localization system.

**The central objective is not just to translate speech, but to generate synchronized, quality-verified dubbed videos while preserving the original video experience.**

---

## 👨‍💻 Author

<div align="center">

### Chandramouli Boppana

**AI/ML Engineer | Generative AI | Agentic AI**

Building intelligent applications at the intersection of AI research, automation, and real-world engineering.

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-chandramouli9392-181717?style=for-the-badge&logo=github)](https://github.com/chandramouli9392)

[![Repository](https://img.shields.io/badge/Project-BodhanAI%20Video%20Dubbing-2ea44f?style=for-the-badge&logo=github)](https://github.com/chandramouli9392/BodhanAI-HighQualityVideoDubbing)

</div>

---

<div align="center">

### 🌏 One Video. Multiple Languages. Seamless Experiences.

**Powered by Bodhan AI | Engineered with Python & FFmpeg**

<br/>

⭐ If you find this project interesting, consider giving the repository a star!

</div>
