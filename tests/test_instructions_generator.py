from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from instructions_generator import InstructionsGenerator
from recording_metadata import RecordingMetadata


class TestGenerate:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.generator = InstructionsGenerator()

    @patch("instructions_generator.Path.write_text")
    @patch("instructions_generator.FILE_TEMPLATE")
    def test_generates_upload_instructions(
        self, mock_template: MagicMock, mock_write_text: MagicMock
    ):
        metadata = RecordingMetadata(
            audio_file_path=Path("sermon.mp3"),
            title="Sunday Sermon",
            date="2026.02.16",
            speaker_name="John Smith",
        )

        self.generator.generate(Path("/output"), metadata)

        mock_template.format.assert_called_once_with(
            soundcloud_track_title="Sunday Sermon // 2026.02.16",
            soundcloud_description="Sunday Sermon // John Smith\nFind out more about River City Church at rivercitydbq.org",
            soundcloud_release_date="2026.02.16",
            youtube_title="Sunday Sermon",
            youtube_description="John Smith // 2026.02.16\nFind out more about River City Church at rivercitydbq.org",
            youtube_recording_date="2026.02.16",
        )
