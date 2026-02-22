from pathlib import Path

import pytest

from recording_metadata import RecordingMetadata
from recording_metadata_validator import RecordingMetadataValidator

@pytest.fixture
def valid_metadata(tmp_path: Path) -> RecordingMetadata:
    audio_file: Path = tmp_path / "sermon.mp3"
    audio_file.touch()
    return RecordingMetadata(
        audio_file_path=audio_file,
        title="Sunday Sermon",
        date="2026.02.16",
        speaker_name="John Smith",
    )

class TestGetErrors:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.validator = RecordingMetadataValidator()

    def test_returns_no_errors_when_valid_metadata_is_provided(self, valid_metadata: RecordingMetadata):
        errors = self.validator.get_errors(valid_metadata)
        assert errors == []

    def test_returns_an_error_when_no_metadata_is_provided(self):
        errors = self.validator.get_errors(None)
        assert errors == ["Please fill out the form"]
    
    def test_returns_an_error_for_each_invalid_metadata_field(self, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("/nonexistent/path/sermon.mp3")
        assert len(self.validator.get_errors(valid_metadata)) == 1
        valid_metadata.title = ""
        assert len(self.validator.get_errors(valid_metadata)) == 2
        valid_metadata.date = ""
        assert len(self.validator.get_errors(valid_metadata)) == 3
        valid_metadata.speaker_name = ""
        assert len(self.validator.get_errors(valid_metadata)) == 4

    def test_returns_an_error_when_metadata_with_empty_file_path_is_provided(self, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("")
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a valid audio file path" in errors

    def test_returns_an_error_when_metadata_with_nonexistent_file_is_provided(self, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("/nonexistent/path/sermon.mp3")
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a valid audio file path" in errors

    def test_returns_an_error_when_metadata_with_empty_title_is_provided(self, valid_metadata: RecordingMetadata):
        valid_metadata.title = ""
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a title" in errors

    def test_returns_an_error_when_metadata_with_empty_date_is_provided(self, valid_metadata: RecordingMetadata):
        valid_metadata.date = ""
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a date in YYYY.MM.DD format" in errors

    @pytest.mark.parametrize("invalid_date", [
        "2026-02-16",
        "02.16.2026",
        "2026.2.16",
        "2026.02.1",
        "2026.02.30",
        "20260216",
        "abcd.ef.gh",
        "2026.02.16.extra",
    ])
    def test_returns_an_error_when_metadata_with_invalid_date_is_provided(self, valid_metadata: RecordingMetadata, invalid_date: str):
        valid_metadata.date = invalid_date
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a date in YYYY.MM.DD format" in errors

    def test_returns_an_error_when_metadata_with_empty_speaker_name_is_provided(self, valid_metadata: RecordingMetadata):
        valid_metadata.speaker_name = ""
        errors = self.validator.get_errors(valid_metadata)
        assert "Please provide a speaker name" in errors
