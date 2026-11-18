from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, model_validator

class WordInfo(BaseModel):
    word: str
    start: float = Field(ge=0.0)
    end: float = Field(ge=0.0)
    confidence: Optional[float] = None

class DubSegment(BaseModel):
    id: str
    start: float = Field(ge=0.0)
    end: float = Field(ge=0.0)
    speaker: Optional[str] = "Speaker_1"
    
    source_text: str = ""
    condensed_text: Optional[str] = None
    translated_text: str = ""
    
    source_language: str = "en"
    target_language: str = "hi"
    
    words: List[WordInfo] = Field(default_factory=list)
    confidence: Optional[float] = None
    
    generated_audio_path: Optional[str] = None
    fitted_audio_path: Optional[str] = None
    
    original_audio_duration: Optional[float] = None
    fitted_audio_duration: Optional[float] = None
    applied_tempo_factor: float = 1.0
    
    # Back-transcription and QA metrics
    back_transcription: Optional[str] = None
    cer: Optional[float] = None
    levenshtein_distance: Optional[int] = None
    qa_status: str = "PENDING"  # ACCEPTED, CONDENSED, RETRIED, MANUAL_REVIEW, REJECTED
    qa_reasons: List[str] = Field(default_factory=list)
    
    retry_count: int = 0
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @property
    def target_duration(self) -> float:
        return max(0.0, self.end - self.start)

    @model_validator(mode="after")
    def validate_times(self):
        if self.end < self.start:
            raise ValueError(f"Segment {self.id}: end time {self.end} is less than start time {self.start}")
        return self

