from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class APIMetric(BaseModel):
    service: str
    endpoint: str
    call_count: int = 0
    total_latency_seconds: float = 0.0
    avg_latency_seconds: float = 0.0
    retry_count: int = 0
    cost_usd: Optional[float] = None
    cost_notes: str = "Pricing tracked or marked unavailable"

class LanguageExecutionSummary(BaseModel):
    language: str
    language_name: str
    status: str = "SUCCESS"  # SUCCESS, FAILED, PARTIAL
    segment_count: int = 0
    accepted_segments: int = 0
    condensed_segments: int = 0
    manual_review_segments: int = 0
    average_cer: Optional[float] = None
    average_tempo_factor: float = 1.0
    min_tempo_factor: float = 1.0
    max_tempo_factor: float = 1.0
    timeline_drift_ms: float = 0.0
    output_video_path: Optional[str] = None
    subtitles_srt_path: Optional[str] = None
    subtitles_vtt_path: Optional[str] = None
    segments_json_path: Optional[str] = None
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)

class DubbingReport(BaseModel):
    pipeline_version: str = "0.1.0"
    timestamp: str
    input_video: str
    original_duration_seconds: float
    output_duration_seconds: float
    duration_difference_ms: float
    duration_within_spec: bool
    target_languages: List[str]
    total_execution_time_seconds: float
    api_metrics: Dict[str, APIMetric] = Field(default_factory=dict)
    languages: Dict[str, LanguageExecutionSummary] = Field(default_factory=dict)
    overall_status: str = "SUCCESS"
    notes: List[str] = Field(default_factory=list)

