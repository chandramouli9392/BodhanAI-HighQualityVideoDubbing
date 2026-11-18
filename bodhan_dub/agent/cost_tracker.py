import time
from typing import Dict, Any, Optional
from bodhan_dub.models.report import APIMetric

class CostAndLatencyTracker:
    """Tracks latency, retry counts, request metrics, and API cost observations."""

    def __init__(self):
        self.metrics: Dict[str, APIMetric] = {
            "transcribe": APIMetric(
                service="Bodhan Indic-Transcribe",
                endpoint="POST /v1/audio/transcriptions",
                cost_notes="Pay-per-minute audio transcription (unverified live rate; marked unbilled in report)"
            ),
            "translate": APIMetric(
                service="Bodhan Indic-Translate",
                endpoint="POST /v1/chat/completions",
                cost_notes="Pay-per-token vLLM translation (unverified live rate; marked unbilled in report)"
            ),
            "speak": APIMetric(
                service="Bodhan Indic-Speak",
                endpoint="POST /v1/audio/speech",
                cost_notes="Pay-per-character audio synthesis (unverified live rate; marked unbilled in report)"
            ),
            "back_transcribe": APIMetric(
                service="Bodhan Indic-Transcribe (QA)",
                endpoint="POST /v1/audio/transcriptions",
                cost_notes="QA verification back-transcription"
            ),
        }

    def record_call(self, service: str, latency: float, retries: int = 0):
        if service not in self.metrics:
            self.metrics[service] = APIMetric(service=service, endpoint="unknown")
        
        m = self.metrics[service]
        m.call_count += 1
        m.total_latency_seconds += latency
        m.avg_latency_seconds = round(m.total_latency_seconds / max(1, m.call_count), 3)
        m.retry_count += retries

    def get_summary(self) -> Dict[str, APIMetric]:
        return self.metrics

