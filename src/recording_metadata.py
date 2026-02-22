from dataclasses import dataclass
from pathlib import Path

@dataclass
class RecordingMetadata:
    audio_file_path: Path
    title: str
    date: str
    speaker_name: str
