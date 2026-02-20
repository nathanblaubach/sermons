import re
from os.path import isfile

from recording_metadata import RecordingMetadata


class RecordingMetadataValidator:
    def get_errors(self, metadata: RecordingMetadata) -> list[str]:
        issues: list[str] = []
        if metadata.audio_file_path == '' or not isfile(metadata.audio_file_path):
            issues.append('Please provide a valid audio file path')
        if metadata.title == '':
            issues.append('Please provide a title')
        if not re.fullmatch(r'\d{4}\.\d{2}\.\d{2}', metadata.date):
            issues.append('Please provide a date in YYYY.MM.DD format')
        if metadata.speaker_name == '':
            issues.append('Please provide a speaker name')
        return issues
