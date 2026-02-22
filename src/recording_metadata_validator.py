import re
from datetime import datetime

from recording_metadata import RecordingMetadata


class RecordingMetadataValidator:
    def get_errors(self, metadata: RecordingMetadata | None) -> list[str]:
        issues: list[str] = []
        if metadata == None:
            return ["Please fill out the form"]
        if not metadata.audio_file_path.is_file():
            issues.append("Please provide a valid audio file path")
        if metadata.title == "":
            issues.append("Please provide a title")
        try:
            if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", metadata.date):
                raise ValueError
            datetime.strptime(metadata.date, "%Y.%m.%d")
        except ValueError:
            issues.append("Please provide a date in YYYY.MM.DD format")
        if metadata.speaker_name == "":
            issues.append("Please provide a speaker name")
        return issues
