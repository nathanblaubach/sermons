from pathlib import Path

import pytest

from recording_metadata import RecordingMetadata
from recording_metadata_validator import RecordingMetadataValidator


@pytest.fixture
def validator() -> RecordingMetadataValidator:
    return RecordingMetadataValidator()


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

class TestValidMetadata:
    def test_returns_no_errors(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        errors = validator.get_errors(valid_metadata)
        assert errors == []

class TestEmptyMetadataValues:
    def test_returns_single_error(self, validator: RecordingMetadataValidator):
        errors = validator.get_errors(None)
        assert errors == ["Please fill out the form"]
        
    def test_empty_file_path_returns_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("")
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a valid audio file path" in errors

    def test_empty_title_returns_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.title = ""
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a title" in errors

    def test_empty_date_returns_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.date = ""
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a date in YYYY.MM.DD format" in errors

    def test_empty_speaker_name_returns_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.speaker_name = ""
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a speaker name" in errors

class TestInvalidFilePathValues:
    def test_nonexistent_file_returns_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("/nonexistent/path/sermon.mp3")
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a valid audio file path" in errors

class TestDate:
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
    def test_invalid_date_formats_return_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata, invalid_date: str):
        valid_metadata.date = invalid_date
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a date in YYYY.MM.DD format" in errors

    @pytest.mark.parametrize("valid_date", [
        "2026.02.16",
        "1999.12.31",
        "2000.01.01",
    ])
    def test_valid_date_formats_return_no_error(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata, valid_date: str):
        valid_metadata.date = valid_date
        errors = validator.get_errors(valid_metadata)
        assert "Please provide a date in YYYY.MM.DD format" not in errors

class TestMultipleErrors:
    def test_all_fields_invalid_returns_all_errors(self, validator: RecordingMetadataValidator, valid_metadata: RecordingMetadata):
        valid_metadata.audio_file_path = Path("/nonexistent/path/sermon.mp3")
        assert len(validator.get_errors(valid_metadata)) == 1
        valid_metadata.title = ""
        assert len(validator.get_errors(valid_metadata)) == 2
        valid_metadata.date = ""
        assert len(validator.get_errors(valid_metadata)) == 3
        valid_metadata.speaker_name = ""
        assert len(validator.get_errors(valid_metadata)) == 4
