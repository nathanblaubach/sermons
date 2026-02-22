from pathlib import Path
from unittest.mock import MagicMock

import pytest

from recording_metadata import RecordingMetadata
from recording_editor import RecordingEditor

class TestPrepareForUpload:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.formMock = MagicMock()
        self.writerMock = MagicMock()
        self.recordingEditor = RecordingEditor(
            self.formMock,
            self.writerMock
        )

    def writes_artifacts_when_metadata_is_provided(self, capsys: pytest.CaptureFixture[str]):
        # Arrange
        metadata = RecordingMetadata(
            audio_file_path=Path("recording.mp3"),
            title="Mark 8:16",
            date="2026.02.22",
            speaker_name="Aaron Morrow",
        )
        self.formMock.get_metadata.return_value = metadata
        self.writerMock.return_value = Path("recording")
        
        # Act
        self.recordingEditor.prepare_for_upload()

        # Assert
        self.writerMock.write.assert_called_once_with(metadata)
        assert str(self.writerMock.write.return_value) in capsys.readouterr().out

    def does_not_write_artifacts_when_no_metadata_is_provided(self):
        # Arrange
        self.formMock = MagicMock()
        writerMock = MagicMock()
        self.formMock.get_metadata.return_value = None

        # Act
        self.recordingEditor.prepare_for_upload()

        # Assert
        writerMock.write.assert_not_called()
