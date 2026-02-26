import shutil
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from instructions_generator import InstructionsGenerator
from recording_metadata import RecordingMetadata
from recording_editor import RecordingEditor
from recording_upload_artifacts_writer import RecordingUploadArtifactsWriter
from video_generator import VideoGenerator


class TestWrite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.formMock = MagicMock()
        self.recordingEditor = RecordingEditor(
            self.formMock,
            RecordingUploadArtifactsWriter(VideoGenerator(), InstructionsGenerator()),
        )

    def test_generates_all_artifacts(self):
        self.formMock.get_metadata.return_value = RecordingMetadata(
            audio_file_path=Path(__file__).parent / "test-recording.mp3",
            title="Test Recording",
            date="2026.02.25",
            speaker_name="Nathan Blaubach",
        )
        expected_destination_directory: Path = Path(__file__).parent / "test-recording"
        if expected_destination_directory.exists():
            shutil.rmtree(expected_destination_directory)

        self.recordingEditor.prepare_for_upload()

        assert all(
            (expected_destination_directory / file_name).is_file()
            for file_name in [
                "soundcloud-artwork.jpg",
                "soundcloud-audio.mp3",
                "upload-instructions.txt",
                "youtube-thumbnail.jpg",
                "youtube-video.mp4",
            ]
        )
