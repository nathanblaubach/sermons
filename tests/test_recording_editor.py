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
        self.recordingEditor = RecordingEditor(self.formMock, self.writerMock)

    def test_writes_artifacts_when_metadata_is_provided(
        self, capsys: pytest.CaptureFixture[str]
    ):
        metadata = RecordingMetadata(
            audio_file_path=Path("recording.mp3"),
            title="Mark 8:16",
            date="2026.02.22",
            speaker_name="Aaron Morrow",
        )
        self.formMock.get_metadata.return_value = metadata
        self.writerMock.return_value = Path("recording")

        self.recordingEditor.prepare_for_upload()

        self.writerMock.write.assert_called_once_with(metadata)
        assert str(self.writerMock.write.return_value) in capsys.readouterr().out

    def test_does_not_write_artifacts_when_no_metadata_is_provided(self):
        self.formMock = MagicMock()
        writerMock = MagicMock()
        self.formMock.get_metadata.return_value = None

        self.recordingEditor.prepare_for_upload()

        writerMock.write.assert_not_called()
