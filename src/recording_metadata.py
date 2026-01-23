from dataclasses import dataclass

@dataclass
class RecordingMetadata:
    audio_file_path: str
    title: str
    date: str
    speaker_name: str
